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

result_1 = 0
result_2 = 0

for k, v in regions.items():
    hedges = set()
    vedges = set()
    for r, c in v:
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if (nr, nc) not in v:
                if dr != 0:
                    hedges.add((dr, dc, nr, nc))
                else:
                    vedges.add((dr, dc, nr, nc))
    # Part 1 counts individual edges
    result_1 += (len(hedges) + len(vedges)) * len(v)

    # Part 2 counts collective edges
    edges = set()

    # Horizontal
    for dr, dc, r, c in hedges:
        rr, cc = r, c
        # Find the right most part of this horizontal edge
        while (dr, dc, rr, cc - 1) in hedges:
            cc -= 1
        hedge = {(dr, dc, rr, cc)}
        while (dr, dc, rr, cc + 1) in hedges:
            hedge.add((dr, dc, rr, cc + 1))
            cc += 1
        edges.add(frozenset(hedge))

    # Vertical
    for dr, dc, r, c in vedges:
        rr, cc = r, c
        # Find the top most part of this vertical edge
        while (dr, dc, rr - 1, cc) in vedges:
            rr -= 1
        vedge = {(dr, dc, rr, cc)}
        while (dr, dc, rr + 1, cc) in vedges:
            vedge.add((dr, dc, rr + 1, cc))
            rr += 1
        edges.add(frozenset(vedge))

    result_2 += len(edges) * len(v)

# Part 1 = 1465112
print(f"answer = {result_1}")

# Part 2 = 893790
print(f"answer = {result_2}")
