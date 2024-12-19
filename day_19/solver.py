import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n\n") if line]
towels = lines[0].split(", ")
patterns = lines[1].split("\n")

result = 0

for p in patterns:
    Q = deque([""])
    seen = set()

    while Q:
        pb = Q.popleft()
        if pb == p:
            result += 1
            break
        if not p.startswith(pb):
            continue
        if pb in seen:
            continue
        seen.add(pb)
        for t in towels:
            Q.append(pb + t)


# Part 1 = 
print(f"answer = {result}")

result = 0

for p in patterns:
    Q = deque([""])
    seen = set()

    while Q:
        pb = Q.popleft()
        if pb == p:
            result += 1
            break
        if not p.startswith(pb):
            continue
        if pb in seen:
            continue
        seen.add(pb)
        for t in towels:
            Q.append(pb + t)


# Part 2 = 
print(f"answer = {result}")
