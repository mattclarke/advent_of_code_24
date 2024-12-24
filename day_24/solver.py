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
for i in lines.split("\n"):
    GATES.append(
        tuple(
            i.replace("-> ", "")
            .replace("x0", "x")
            .replace("y0", "y")
            .replace("z0", "z")
            .split(" ")
        )
    )

values = copy.copy(VALUES)
gates = deque(GATES[:])

while gates:
    a, cmd, b, c = gates.popleft()
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
        gates.append((a, cmd, b, c))

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


def solve(values, gates, x, y):
    x = f"{x:045b}"
    y = f"{y:044b}"
    for i, xx, yy in enumerate(zip(reversed(x), reversed(y))):
        pass

    while gates:
        a, cmd, b, c = gates.popleft()
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
            gates.append((a, cmd, b, c))


# Part 2 =
print(f"answer = {result}")
