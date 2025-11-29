import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

data = []
for l in lines:
    data.append([int(x) for x in l.replace(":", "").split(" ")])

result = 0

for d in data:
    found = False
    total = d[0]
    Q = deque()
    Q.append((d[1], 1))
    while Q:
        v, i = Q.popleft()
        if i + 1 == len(d):
            continue
        nxt = d[i + 1]

        branches = [v + nxt, v * nxt]

        if i + 1 == len(d) - 1:
            if total in branches:
                found = True
                break

        for b in branches:
            if b <= total:
                Q.append((b, i + 1))
    if found:
        result += total

# Part 1 = 882304362421
print(f"answer = {result}")

result = 0

for d in data:
    found = False
    total = d[0]
    Q = deque()
    Q.append((d[1], 1))
    while Q:
        v, i = Q.popleft()
        if i + 1 == len(d):
            continue
        nxt = d[i + 1]

        branches = [v + nxt, v * nxt, int(str(v) + str(nxt))]

        if i + 1 == len(d) - 1:
            if total in branches:
                found = True
                break

        for b in branches:
            if b <= total:
                Q.append((b, i + 1))
    if found:
        result += total

# Part 2 = 145149066755184
print(f"answer = {result}")
