import copy
import sys
from collections import defaultdict


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]
layout = {}
antennas = defaultdict(list)

for r, l in enumerate(lines):
    for c, ch in enumerate(l):
        layout[r, c] = ch
        if ch != ".":
            a = antennas[ch]
            a.append((r, c))
            antennas[ch] = a

result = 0

locs = set()
for k, v in antennas.items():
    for i, a in enumerate(v):
        for j in range(i + 1, len(v)):
            b = v[j]
            my = abs(a[0] - b[0])
            mx = abs(a[1] - b[1])
            if a[0] < b[0]:
                ny1 = a[0] - my
                ny2 = b[0] + my
                if a[1] < b[1]:
                    nx1 = a[1] - mx
                    nx2 = b[1] + mx
                else:
                    nx1 = a[1] + mx
                    nx2 = b[1] - mx
                if (ny1, nx1) in layout:
                    locs.add((ny1, nx1))
                if (ny2, nx2) in layout:
                    locs.add((ny2, nx2))
            else:
                ny1 = a[0] + my
                ny2 = b[0] - my
                if a[1] < b[1]:
                    nx1 = a[1] - mx
                    nx2 = b[1] + mx
                else:
                    nx1 = a[1] + mx
                    nx2 = b[1] - mx
                if (ny1, nx1) in layout:
                    locs.add((ny1, nx1))
                if (ny2, nx2) in layout:
                    locs.add((ny2, nx2))

result = len(locs)


# Part 1 = 222
print(f"answer = {result}")

result = 0

# Part 2 =
print(f"answer = {result}")
