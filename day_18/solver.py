import copy
import heapq
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

result = 0
corrupted = []

for line in lines:
    x, y = [int(x) for x in line.split(",")]
    corrupted.append((x, y))

pos = (0, 0)
goal = (70, 70)

part_1_corrupted = set()
for c in corrupted[:1024]:
    part_1_corrupted.add(c)

occupied = {pos}
result = 0
while goal not in occupied:
    new_occupied = set()
    for o in occupied:
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = o[0] + dx
            ny = o[1] + dy
            if nx < 0 or nx > 70:
                continue
            if ny < 0 or ny > 70:
                continue
            if (nx, ny) in part_1_corrupted:
                continue
            new_occupied.add((nx, ny))
    occupied = new_occupied
    result += 1

# Part 1 = 314
print(f"answer = {result}")

pos = (0, 0)
size = 70
goal = (size, size)

part_2_corrupted = corrupted[:1024]

while True:
    Q = [pos]
    seen = set()
    at_goal = False
    while Q and not at_goal:
        x, y = heapq.heappop(Q)
        x, y = -x, -y
        if (x, y) == goal:
            at_goal = True
            continue
        if (x, y) in seen:
            continue
        if (x, y) in part_2_corrupted:
            continue
        seen.add((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx > size:
                continue
            if ny < 0 or ny > size:
                continue
            heapq.heappush(Q, (-nx, -ny))
    if not at_goal:
        result = part_2_corrupted[~0]
        break
    part_2_corrupted.append(corrupted.pop(0))

# Part 2 = 15, 20
print(f"answer = {result}")
