import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line][0]
NUMBERS = [int(x) for x in lines.split(" ")]


def process(n):
    new_numbers = []
    sn = str(n)
    if n == 0:
        new_numbers.append(1)
    elif len(sn) % 2 == 0:
        half = len(sn) // 2
        a = sn[:half]
        b = sn[half:]
        new_numbers.append(int(a))
        new_numbers.append(int(b))
    else:
        new_numbers.append(n * 2024)
    return new_numbers


numbers = NUMBERS[:]

for i in range(25):
    new_numbers = []
    for n in numbers:
        new_numbers.extend(process(n))
    numbers = new_numbers

# Part 1 = 194482
print(f"answer = {len(numbers)}")

DP = {}


def solve(node):
    if node in DP:
        return DP[node]
    if node[2] >= 75:
        if node not in DP:
            DP[node] = node[1]
        return node[1]
    new_numbers = process(node[0])
    unique = set(new_numbers)
    total = 0
    for u in unique:
        nnode = (u, new_numbers.count(u), node[2] + 1)
        total += solve(nnode)
    if node not in DP:
        DP[node] = node[1] * total
    return node[1] * total


result = 0
for n in NUMBERS:
    # value, multiplier, depth
    root = (n, 1, 0)
    result += solve(root)

# Part 1 = 232454623677743
print(f"answer = {result}")
