import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [int(line.strip()) for line in PUZZLE_INPUT.split("\n") if line]


def generate(sn):
    sn ^= sn * 64
    sn %= 16777216
    sn ^= sn // 32
    sn %= 16777216
    sn ^= sn * 2048
    sn %= 16777216
    return sn


result = 0

for i, line in enumerate(lines):
    sn = line
    for _ in range(2000):
        sn = generate(sn)
    result += sn

# Part 1 = 18525593556
print(f"answer = {result}")

result = 0

sn = lines[0]
seen = set()
values = []
diffs = []
last = lines[0] % 10
for i in range(16777217):
    sn = generate(sn)
    if sn in seen:
        break
    seen.add(sn)
    values.append(sn)
    diffs.append(sn % 10 - last)
    last = sn % 10

offsets = []
for i, line in enumerate(lines):
    sn = generate(line)
    found = values.index(sn)
    offsets.append(found)

best = 0
for i in range(3, 2000):
    v = values[i] % 10
    d = [diffs[i - 3], diffs[i - 2], diffs[i - 1], diffs[i]]
    result = 0
    for o in offsets:
        for j in range(o, o + 2000 - 3):
            if (
                d[0] == diffs[j]
                and d[1] == diffs[j + 1]
                and d[2] == diffs[j + 2]
                and d[3] == diffs[j + 3]
            ):
                result += (values[j + 3]) % 10
                break
    if result > best:
        best = result

# Part 2 = 2089
print(f"answer = {best}")
