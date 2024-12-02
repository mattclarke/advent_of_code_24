import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]


def is_valid(vals):
    diffs = []
    for i in range(len(vals) - 1):
        d = vals[i + 1] - vals[i]
        diffs.append(d)
    ascending = None
    valid = True
    for d in diffs:
        if d == 0:
            valid = False
            break
        if ascending is None:
            if d > 0:
                ascending = True
            else:
                ascending = False
        if ascending and d < 0:
            valid = False
            break
        if not ascending and d > 0:
            valid = False
            break
        if abs(d) > 3:
            valid = False
            break
    return valid


result = 0

for l in lines:
    vals = l.split(" ")
    vals = [int(x) for x in vals]
    if is_valid(vals):
        result += 1

# Part 1 = 411
print(f"answer = {result}")

result = 0

for l in lines:
    vals = l.split(" ")
    vals = [int(x) for x in vals]
    for i in range(len(vals)):
        temp = vals[:i] + vals[i + 1:]
        if is_valid(temp):
            result += 1
            break

# Part 2 = 465
print(f"answer = {result}")
