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


diff_to_value = {}
result = 0

for i, line in enumerate(lines):
    sn = line
    seen = set()
    Q = deque([])
    last = line % 10
    for _ in range(2000):
        sn = generate(sn)
        Q.append((sn % 10) - last)
        last = sn % 10
        if len(Q) > 4:
            Q.popleft()
        if len(Q) == 4:
            t = tuple(Q)
            if t not in seen:
                seen.add(t)
                diff_to_value[t] = diff_to_value.get(t, 0) + last
    result += sn

# Part 1 = 18525593556
print(f"answer = {result}")

result = max(diff_to_value.values())

# Part 2 = 2089
print(f"answer = {result}")
