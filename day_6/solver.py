import copy
from collections import defaultdict
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

layout = {}
result = 0
START = None

for r, l in enumerate(lines):
    for c, ch in enumerate(l):
        if ch == "^":
            START = (r, c)
            layout[r,c] = "."
            continue
        layout[r,c] = ch

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

pos = START
visited = defaultdict(lambda: 0)
visited[START] = 1
direction = 0

while True:
    new_pos = (pos[0] + DIRS[direction][0], pos[1] + DIRS[direction][1])
    if new_pos not in layout:
        break
    if layout[new_pos] == ".":
        visited[new_pos] = visited[new_pos] + 1
        pos = new_pos
    else:
        direction = (direction + 1) % len(DIRS)

result = len(visited)

# Part 1 = 4988
print(f"answer = {result}")

result = 0

# Part 2 = 
print(f"answer = {result}")
