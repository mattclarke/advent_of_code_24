import copy
import re
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]
print(len(lines))

result = 0

for l in lines:
    m = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", l)
    for a, b in m:
        result += int(a) * int(b)

# Part 1 = 174960292
print(f"answer = {result}")

result = 0
do = True

# Insert | between the lines to avoid a line ending with do and the next starting with n't()
m = re.findall(r"(do)\(\)|(don't)\(\)|mul\((\d{1,3}),(\d{1,3})\)", "|".join(lines))

for d, dn, a, b in m:
    if d:
        do = True
    elif dn:
        do = False
    elif do:
        result += int(a) * int(b)

# Part 2 = 56275602
print(f"answer = {result}")
