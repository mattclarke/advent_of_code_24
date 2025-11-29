import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n\n") if line]

locks = []
keys = []

for line in lines:
    is_lock = False
    values = [-1, -1, -1, -1, -1]
    for i, ll in enumerate(line.split("\n")):
        if i == 0 and ll == "#####":
            is_lock = True
        for j, ch in enumerate(ll):
            if ch == "#":
                values[j] += 1
    if is_lock:
        locks.append(values)
    else:
        keys.append(values)

result = 0

for lk in locks:
    for k in keys:
        fail = False
        for i in range(5):
            if lk[i] + k[i] > 5:
                fail = True
        if not fail:
            result += 1

# Part 1 = 3057
print(f"answer = {result}")
