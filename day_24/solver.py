import copy
import random
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

initial, lines = [line.strip() for line in PUZZLE_INPUT.split("\n\n") if line]

VALUES = {}
for i in initial.split("\n"):
    n, v = i.split(": ")
    VALUES[n] = int(v)

GATES = []
OUTPUTS = []
for i in lines.split("\n"):
    a, cmd, b, c = i.replace("-> ", "").split(" ")
    GATES.append((a, cmd, b))
    OUTPUTS.append(c)

values = copy.copy(VALUES)
gates = deque(GATES[:])
outputs = deque(OUTPUTS[:])

while gates:
    a, cmd, b = gates.popleft()
    c = outputs.popleft()
    if a in values and b in values:
        if cmd == "OR":
            values[c] = values[a] | values[b]
        elif cmd == "AND":
            values[c] = values[a] & values[b]
        elif cmd == "XOR":
            values[c] = values[a] ^ values[b]
        else:
            assert False
    else:
        gates.append((a, cmd, b))
        outputs.append(c)

zeds = []
for i in range(100):
    z = f"z{i:02}"
    if z not in values:
        break
    zeds.append(str(values[z]))

zeds.reverse()
zedstr = "".join(zeds)
result = int(zedstr, 2)

# Part 1 = 45923082839246
print(f"answer = {result}")
assert result == 45923082839246


def solve(values, gates, outputs, x, y):
    x = f"{x:045b}"
    y = f"{y:045b}"
    for i, (xx, yy) in enumerate(zip(reversed(x), reversed(y))):
        values[f"x{i:02}"] = int(xx)
        values[f"y{i:02}"] = int(yy)

    num_gates = len(gates)
    loop_count = 0

    while gates:
        a, cmd, b = gates.popleft()
        c = outputs.popleft()
        if a in values and b in values:
            if cmd == "OR":
                values[c] = values[a] | values[b]
            elif cmd == "AND":
                values[c] = values[a] & values[b]
            elif cmd == "XOR":
                values[c] = values[a] ^ values[b]
            else:
                assert False
            num_gates = len(gates)
            loop_count = 0
        else:
            gates.append((a, cmd, b))
            outputs.append(c)
        if loop_count > num_gates:
            # Infinite loop
            return None, None
        loop_count += 1
    zeds = []
    for i in range(100):
        z = f"z{i:02}"
        if z not in values:
            break
        zeds.append(str(values[z]))

    zeds.reverse()
    zedstr = "".join(zeds)
    return int(zedstr, 2), zedstr


def test_solution(outputs, z):
    for i in range(1000):
        r = random.randint(0, 2**z - 1)
        s = random.randint(0, 2**z - 1)
        ans, _ = solve(copy.copy(VALUES), deque(GATES[:]), deque(outputs[:]), r, s)
        if ans != r + s:
            return False
    return True


max_value = 2**45 - 1


def recursive(outputs, swapped):
    print(swapped)
    num, zeds = solve(
        copy.copy(VALUES), deque(GATES[:]), deque(outputs[:]), max_value, 0
    )
    if num == max_value:
        if test_solution(outputs, 45):
            result = copy.copy(swapped)
            return True, swapped
    else:
        # Find first incorrect value
        z = 45 - zeds.rfind("0")
        outputs = outputs[:]
        for i, o1 in enumerate(outputs):
            if o1 in swapped:
                continue
            for j, o2 in enumerate(outputs):
                if j <= i:
                    continue
                if o2 in swapped:
                    continue
                outputs[i], outputs[j] = outputs[j], outputs[i]
                nz, nzeds = solve(
                    copy.copy(VALUES), deque(GATES[:]), deque(outputs[:]), max_value, 0
                )
                if nz:
                    uz = 45 - nzeds.rfind("0")
                    if uz > z:
                        if test_solution(outputs, z):
                            valid, result = recursive(
                                outputs, swapped.union({outputs[i], outputs[j]})
                            )
                            if valid:
                                return True, result
                outputs[i], outputs[j] = outputs[j], outputs[i]
    return False, set()


_, result = recursive(OUTPUTS[:], set())
result = ','.join(sorted(list(result)))

# Part 2 = jgb,rkf,rrs,rvc,vcg,z09,z20,z24
print(f"answer = {result}")
assert result == "jgb,rkf,rrs,rvc,vcg,z09,z20,z24"
