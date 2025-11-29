import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n\n") if line]
towels = lines[0].split(", ")
patterns = lines[1].split("\n")


def solve(pattern, towels, sofar, seen):
    if sofar in seen:
        return seen[sofar]
    if sofar == pattern:
        return 1
    if not pattern.startswith(sofar):
        return 0
    total = 0
    for t in towels:
        total += solve(pattern, towels, sofar + t, seen)
    seen[sofar] = total
    return total


result_1 = 0
result_2 = 0

for p in patterns:
    seen = {}
    ans = solve(p, towels, "", seen)
    result_1 += 1 if ans else 0
    result_2 += ans

# Part 1 = 269
print(f"answer = {result_1}")

# Part 2 = 758839075658876
print(f"answer = {result_2}")
