import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

layout = {}
start = None
end = None
D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for r, l in enumerate(lines):
    for c, ch in enumerate(l):
        if ch == "S":
            start = (r, c)
            layout[r, c] = "."
        elif ch == "E":
            end = (r, c)
            layout[r, c] = "."
        else:
            layout[r, c] = ch

Q = deque([(start, 0, 0)])
SEEN = {}
result = 10000000000000000000000

while Q:
    pos, d, score = Q.popleft()
    if (pos, d) in SEEN and score >= SEEN[(pos, d)]:
        continue
    SEEN[(pos, d)] = score
    if pos == end:
        result = min(score, result)
        continue
    dr, dc = D[d]
    if layout[pos[0] + dr, pos[1] + dc] == ".":
        Q.append(((pos[0] + dr, pos[1] + dc), d, score + 1))
    dr, dc = D[(d - 1) % 4]
    if layout[pos[0] + dr, pos[1] + dc] == ".":
        Q.append(((pos[0] + dr, pos[1] + dc), (d - 1) % 4, score + 1001))
    dr, dc = D[(d + 1) % 4]
    if layout[pos[0] + dr, pos[1] + dc] == ".":
        Q.append(((pos[0] + dr, pos[1] + dc), (d + 1) % 4, score + 1001))


# Part 1 = 105496
print(f"answer = {result}")

result = 0

# Part 2 =
print(f"answer = {result}")
