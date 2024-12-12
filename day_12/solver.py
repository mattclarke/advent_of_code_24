import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]
layout = {}

for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        layout[r, c] = ch

seen = set()
regions = {}
count = 0

for r in range(len(lines)):
    for c in range(len(lines[0])):
        if (r, c) in seen:
            continue
        region = {(r, c)}
        name = layout[r, c]
        q = [(r, c)]
        while q:
            curr = q.pop(0)
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr = curr[0] + dr
                nc = curr[1] + dc
                if (nr, nc) in seen:
                    continue
                if layout.get((nr, nc)) != name:
                    continue
                region.add((nr, nc))
                q.append((nr, nc))
                seen.add((nr, nc))
        regions[count] = region
        count += 1


edges = {}
for k, v in regions.items():
    nedges = 0
    for r, c in v:
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if (nr, nc) not in v:
                nedges += 1
    edges[k] = nedges

result = 0
for k, v in regions.items():
    result += len(v) * edges[k]
# Part 1 = 1465112
print(f"answer = {result}")

result = 0

# Part 2 =
print(f"answer = {result}")
