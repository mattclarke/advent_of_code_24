import copy
import sys
from collections import deque, defaultdict


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

result = 0

layout = defaultdict(set)
tees = set()

for line in lines:
    a, b = line.split("-")
    layout[a].add(b)
    layout[b].add(a)
    if a.startswith("t"):
        tees.add(a)
    if b.startswith("t"):
        tees.add(b)

solutions = set()

for t in tees:
    nodes = layout[t]
    for n in nodes:
        nodes2 = layout[n]
        for nn in nodes2:
            if n == nn or nn == t:
                continue
            if t in layout[nn]:
                solutions.add(frozenset({t, n, nn}))


# Part 1 = 1218
print(f"answer = {len(solutions)}")

result = 0

# Part 2 =
print(f"answer = {result}")
