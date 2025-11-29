import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]


a = []
b = []

for l in lines:
    f, s = l.split("   ")
    a.append(int(f))
    b.append(int(s))

a.sort()
b.sort()

result = 0

for f, s in zip(a, b):
    result += abs(f - s)

# Part 1 = 2430334
print(f"answer = {result}")

result = 0
for f in a:
    result += b.count(f) * f

# Part 2 = 28786472
print(f"answer = {result}")
