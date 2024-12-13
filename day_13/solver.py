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

MAX_SCORE = 100000000000000000


def solve_1(a, b, p, nmax):
    DP = {}
    best = MAX_SCORE
    Q = deque([(0, 0, 0, 0)])
    while Q:
        x, y, na, nb = Q.popleft()
        if (x, y) == p:
            best = min(best, na * 3 + nb)
            continue
        if na >= nmax or nb >= nmax:
            continue
        if DP.get((x, y), MAX_SCORE) <= na * 3 + nb:
            continue
        if x > p[0] or y > p[1]:
            continue
        DP[x, y] = na * 3 + nb
        Q.append((x + a[0], y + a[1], na + 1, nb))
        Q.append((x + b[0], y + b[1], na, nb + 1))
    return best


result = 0

for pu in puzzle:
    a, b, p = pu
    ans = solve_1(a, b, p, 100)
    if ans < MAX_SCORE:
        result += ans


# Part 1 = 29711
print(f"answer = {result}")

result = 0

# Part 2 =
print(f"answer = {result}")
