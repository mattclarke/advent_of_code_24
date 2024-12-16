import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]
print(lines)

result = 0

for line in lines:
    pass

# Part 1 = 
print(f"answer = {result}")

result = 0

# Part 2 = 
print(f"answer = {result}")
