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
    VALUES[n] = int(v)

GATES = []
for i in lines.split("\n"):
    GATES.append(tuple(i.replace("-> ", "").split(" ")))

result = 0
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
    if i < 10:
        z += "0" + str(i)
    else:
        z += str(i)
    if z not in values:
        print(f"max z is {z}")
        break
    zeds.append(str(values[z]))

zeds.reverse()
zedstr = "".join(zeds)
result = int(zedstr, 2)

# Part 1 = 45923082839246
print(f"answer = {result}")

result = 0

# Part 2 =
print(f"answer = {result}")
