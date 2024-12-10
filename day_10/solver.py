import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

layout = {}
starts = set()

for r, l in enumerate(lines):
    for c, ch in enumerate(l):
        layout[r, c] = int(ch)
        if ch == "0":
            starts.add((r, c))

D = [(0, -1), (-1, 0), (1, 0), (0, 1)]
result = 0

for start in starts:
    peaks = set()
    Q = deque([start])
    while Q:
        pos = Q.popleft()
        value = layout[pos]
        if value == 9:
            peaks.add(pos)
            continue
        for r, c in D:
            nr = pos[0] + r
            nc = pos[1] + c
            if layout.get((nr, nc)) == value + 1:
                Q.append((nr, nc))
    result += len(peaks)

# Part 1 = 517
print(f"answer = {result}")

result = 0

# Part 2 =
print(f"answer = {result}")
