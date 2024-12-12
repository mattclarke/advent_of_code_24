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

edges = {}
for k, v in regions.items():
    hedges = set()
    vedges = set()
    for r, c in v:
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if (nr, nc) not in v:
                if dr != 0:
                    hedges.add((dr, nr, nc))
                else:
                    vedges.add((dc, nr, nc))

    nedges = 0
    # Horizontal
    temp1 = set()
    for d, r, c in hedges:
        rr, cc = r, c
        while (d, rr, cc - 1) in hedges:
            cc -= 1
        hedge = {(d, rr, cc)}
        while (d, rr, cc + 1) in hedges:
            hedge.add((d, rr, cc + 1))
            cc += 1
        fro = frozenset(hedge)
        temp1.add(fro)

    # Vertical
    temp2 = set()
    for d, r, c in vedges:
        rr, cc = r, c
        while (d, rr - 1, cc) in vedges:
            rr -= 1
        vedge = {(d, rr, cc)}
        while (d, rr + 1, cc) in vedges:
            vedge.add((d, rr + 1, cc))
            rr += 1
        fro = frozenset(vedge)
        temp2.add(fro)
    edges[k] = len(temp1) + len(temp2)

result = 0

for k, v in regions.items():
    result += len(v) * edges[k]

# Part 2 = 893790
print(f"answer = {result}")
