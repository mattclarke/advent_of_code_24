import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n\n") if line]

puzzle = []
for ls in lines:
    ls = (
        ls.replace("Button A: ", "")
        .replace("Button B: ", "")
        .replace("Prize: ", "")
        .replace(",", "")
        .replace("X=", "")
        .replace("Y=", "")
        .replace("X+", "")
        .replace("Y+", "")
    )
    a, b, p = ls.split("\n")
    a = tuple([int(x) for x in a.split(" ")])
    b = tuple([int(x) for x in b.split(" ")])
    p = tuple([int(x) for x in p.split(" ")])
    puzzle.append((a, b, p))


def solve_a(i, xa, ya, xb, yb, yt):
    return i * xa + ((yt - i * ya) / yb) * xb


result = 0

for pu in puzzle:
    a, b, p = pu
    num_a = None
    for i in range(100):
        ans = solve_a(i, a[0], a[1], b[0], b[1], p[1])
        if ans == p[0]:
            num_a = i
            break
    if num_a is not None:
        diff = p[0] - (a[0] * num_a)
        num_b = diff / b[0]
        result += num_a * 3 + num_b

# Part 1 = 29711
print(f"answer = {int(result)}")

result = 0


def binary_search(a, b, p):
    low = 1
    high = 10000000000000
    # Need to check for inversion
    lowest = solve_a(low, a[0], a[1], b[0], b[1], p[1])
    highest = solve_a(high, a[0], a[1], b[0], b[1], p[1])
    if lowest < highest:
        while low != high:
            mid = low + (high - low) // 2
            ans = solve_a(mid, a[0], a[1], b[0], b[1], p[1])
            if ans < p[0]:
                low = mid + 1
            elif ans > p[0]:
                high = mid
            else:
                return mid
        return None
    else:
        while low != high:
            mid = low + (high - low) // 2
            ans = solve_a(mid, a[0], a[1], b[0], b[1], p[1])
            if ans > p[0]:
                low = mid + 1
            elif ans < p[0]:
                high = mid
            else:
                return mid
        return None


for pu in puzzle:
    a, b, p = pu
    p = (p[0] + 10000000000000, p[1] + 10000000000000)
    num_a = binary_search(a, b, p)
    if num_a is not None:
        diff = p[0] - (a[0] * num_a)
        num_b = diff / b[0]
        result += num_a * 3 + num_b

# Part 2 = 94955433618919
print(f"answer = {int(result)}")
