import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

initial, lines = [line.strip() for line in PUZZLE_INPUT.split("\n\n") if line]

VALUES = {}
for i in initial.split("\n"):
    n, v = i.split(": ")
    n = n.replace("x0", "x").replace("y0", "y")
    VALUES[n] = int(v)

GATES = []
OUTPUTS = []
counts = {}
for i in lines.split("\n"):
    a, cmd, b, c = i.replace("-> ", "") .replace("x0", "x") .replace("y0", "y") .replace("z0", "z") .split(" ")
    GATES.append((a,cmd,b))
    OUTPUTS.append(c)

    if a[0] not in ["x", "y", "z"]:
        counts[a] = counts.get(a, 0) + 1
    if b[0] not in ["x", "y", "z"]:
        counts[b] = counts.get(b, 0) + 1
    if c[0] not in ["x", "y", "z"]:
        counts[c] = counts.get(c, 0) + 1

print(len(counts))
print(max(counts.values()))

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
    z = "z"
    z += str(i)
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
    print(x, y, x+y)
    x = f"{x:045b}"
    y = f"{y:045b}"
    print(f" {x}")
    print(f" {y}")
    for i, (xx, yy) in enumerate(zip(reversed(x), reversed(y))):
        values[f"x{i}"] = int(xx)
        values[f"y{i}"] = int(yy)

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
        z = "z"
        z += str(i)
        if z not in values:
            break
        zeds.append(str(values[z]))

    zeds.reverse()
    zedstr = "".join(zeds)
    print(zedstr)
    # print(values["x1"], values["y1"], values["rdj"], values["mjh"], values["z1"], values["tqp"])
    return int(zedstr, 2)


# print(solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), 0, 0))
# print(solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), 1, 1))
# print(solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), 2, 0))
# print(solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), 3, 1))
# print(solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), 2, 2))
# print(solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), 3, 2))
# print(solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), 3, 3))
# print(solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), 4, 3))
# print(solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), 4, 4))
# print(solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), 5, 4))
# print(solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), 8, 5))
# print(solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), 9, 8))

wrong = set()
for i in range(44):
    ans = solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), 1 << i, 0)
    if ans != (1 << i):
        wrong.add(i)

print(len(wrong), wrong)

top = 2**45 - 1
print(solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), top, 0))

z09 = OUTPUTS.index("z9")
wpr = OUTPUTS.index("rkf")
OUTPUTS[z09], OUTPUTS[wpr] = OUTPUTS[wpr], OUTPUTS[z09]
print(solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), top, 0))
print(solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), 337, 426))

#1110010100
#0011101001

print(z09, wpr)
for i in range(1000):
    import random
    r = random.randint(0, 2**9-1)
    s = random.randint(0, 2**9-1)
    ans = solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), r, s)
    if ans != r+s:
        assert False, f"ans1 = {ans}"

z20 = OUTPUTS.index("z20")
qkq = OUTPUTS.index("jgb")

OUTPUTS[z20], OUTPUTS[qkq] = OUTPUTS[qkq], OUTPUTS[z20]
print(solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), top, 0))
for i in range(1000):
    import random
    r = random.randint(0, 2**20-1)
    s = random.randint(0, 2**20-1)
    ans = solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), r, s)
    if ans != r+s:
        assert False, f"ans2 = {ans}"


z20 = OUTPUTS.index("z24")
qkq = OUTPUTS.index("vcg")

OUTPUTS[z20], OUTPUTS[qkq] = OUTPUTS[qkq], OUTPUTS[z20]
print(solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), top, 0))
for i in range(1000):
    import random
    r = random.randint(0, 2**24-1)
    s = random.randint(0, 2**24-1)
    ans = solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), r, s)
    if ans != r+s:
        assert False, f"ans3 = {ans}"

z20 = OUTPUTS.index("rrs")
qkq = OUTPUTS.index("rvc")

OUTPUTS[z20], OUTPUTS[qkq] = OUTPUTS[qkq], OUTPUTS[z20]
print(solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), top, 0))

for i in range(1000):
    import random
    r = random.randint(0, 2**44-1)
    s = random.randint(0, 2**44-1)
    ans = solve(copy.copy(VALUES), deque(GATES[:]), deque(OUTPUTS[:]), r, s)
    if ans != r+s:
        assert False, f"ans = {ans}"

# Part 2 = jgb,rkf,rrs,rvc,vcg,z09,z20,z24
print(f"answer = {result}")
