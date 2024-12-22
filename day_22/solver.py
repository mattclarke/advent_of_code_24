import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [int(line.strip()) for line in PUZZLE_INPUT.split("\n") if line]
print(lines)

result = 0

for line in lines:
    sn = line
    for _ in range(2000):
        sn ^= sn * 64
        sn %= 16777216
        sn ^= sn // 32
        sn %= 16777216
        sn ^= sn * 2048
        sn %= 16777216
    result += sn


# Part 1 = 18525593556
print(f"answer = {result}")

result = 0

# Part 2 =
print(f"answer = {result}")
