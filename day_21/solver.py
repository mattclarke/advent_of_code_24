import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]
print(lines)

num_pad = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "": (3, 0),
    "0": (3, 1),
    "A": (3, 2),
}


dpad = {
    "": (0, 0),
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}


def solve_numpad(code):
    Q = deque([(num_pad["A"], 0, "")])
    best = 100000000
    results = []
    while Q:
        (r, c), n, route = Q.popleft()
        if (r, c) == (3, 0):
            continue
        if n == len(code):
            if len(route) < best:
                best = len(route)
                results = []
            results.append(route)
            continue
        nr, nc = num_pad[code[n]]
        if (r, c) == (nr, nc):
            Q.append(((r, c), n + 1, route + "A"))
            continue

        if nr > r:
            Q.append(((r + 1, c), n, route + "v"))
        if nr < r:
            Q.append(((r - 1, c), n, route + "^"))
        if nc > c:
            Q.append(((r, c + 1), n, route + ">"))
        if nc < c:
            Q.append(((r, c - 1), n, route + "<"))

    return results


def solve_dpad(code, best=1000000000):
    Q = deque([(dpad["A"], 0, "")])
    results = []
    while Q:
        (r, c), n, route = Q.popleft()
        if (r, c) == (0, 0):
            continue
        if len(route) > best:
            continue
        if n == len(code):
            if len(route) < best:
                best = len(route)
                results = []
            results.append(route)
            continue
        nr, nc = dpad[code[n]]
        if (r, c) == (nr, nc):
            Q.append(((r, c), n + 1, route + "A"))
            continue

        if nr > r:
            Q.append(((r + 1, c), n, route + "v"))
        if nr < r:
            Q.append(((r - (r - nr), c), n, route + "^" * (r - nr)))
        if nc > c:
            Q.append(((r, c + (nc - c)), n, route + ">" * (nc - c)))
        if nc < c:
            Q.append(((r, c - 1), n, route + "<"))

    return results


result = 0
for line in lines:
    print(line)
    ans = solve_numpad(line)

    temp = ans
    for _ in range(2):
        best = 100000000000000000000000000
        new_t = []
        for t in temp:
            a = solve_dpad(t)
            if a:
                best = min(best, len(a[0]))
            new_t.extend(a)
        temp = new_t

    result += best * int(line.replace("A", ""))
    print(best)
    print("=================")

# Part 1 = 156714
print(f"answer = {result}")

result = 0

# Part 2 =
print(f"answer = {result}")
