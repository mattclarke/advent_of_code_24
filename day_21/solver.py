import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

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


moves = {
    "A",
    "vA",
    ">A",
    "^A",
    "<A",
    "<vA",
    "v>A",
    "v<A",
    "<<A",
    "<^A",
    ">^A",
    ">>A",
    "^>A",
    "^<A",
    ">vA",
    "v<<A",
    ">>^A",
    "<v<A",
    ">^>A",
}


def solve_dpad(code):
    best = 100000000000000
    Q = deque([(dpad["A"], 0, "")])
    results = set()
    while Q:
        (r, c), n, route = Q.popleft()
        if (r, c) == (0, 0):
            continue
        if n == len(code):
            if len(route) < best:
                best = len(route)
                results = set()
            results.add(route)
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


# def solve_dpad(code):
#     current = "A"
#     result = ""
#     for c in code:
#         if current == "A" and c == "<":
#             result += "v<<"
#         elif current == "A" and c == "v":
#             result += "<v"
#         elif current == "A" and c == "^":
#             result += "<"
#         elif current == "A" and c == ">":
#             result += "v"
#
#         elif current == "^" and c == "<":
#             result += "v<"
#         elif current == "^" and c == "v":
#             result += "v"
#         elif current == "^" and c == "A":
#             result += ">"
#         elif current == "^" and c == ">":
#             result += "v>"
#
#         elif current == ">" and c == "<":
#             result += "<<"
#         elif current == ">" and c == "v":
#             result += "<"
#         elif current == ">" and c == "A":
#             result += "^"
#         elif current == ">" and c == "^":
#             result += "<^"
#
#         elif current == "v" and c == "<":
#             result += "<"
#         elif current == "v" and c == "^":
#             result += "^"
#         elif current == "v" and c == "A":
#             result += "^>"
#         elif current == "v" and c == ">":
#             result += ">"
#
#         elif current == "<" and c == "v":
#             result += ">"
#         elif current == "<" and c == "^":
#             result += ">^"
#         elif current == "<" and c == "A":
#             result += ">>^"
#         elif current == "<" and c == ">":
#             result += ">>"
#         elif current == c:
#             pass
#         else:
#             assert False, f"{current}, {c}"
#         result += "A"
#         current = c
#     return {result}


result = 0
for line in lines:
    best = 1000000000000
    for a in solve_numpad(line):
        for aa in solve_dpad(a):
            for aaa in solve_dpad(aa):
                best = min(best, len(aaa))
    result += best * int(line.replace("A", ""))

# Part 1 = 156714
print(f"answer = {result}")


def breakup(code):
    counter = {}
    while code:
        for m in moves:
            if code.startswith(m):
                code = code[len(m):]
                counter[m] = counter.get(m, 0) + 1
                break
    return counter


seen = {}


def solve(code, n):
    if n == 0:
        return len(code)
    if (code, n) in seen:
        return seen[code, n]
    minimum = 10000000000000000000
    for ncode in solve_dpad(code):
        result = 0
        counter = breakup(ncode)
        for k, v in counter.items():
            result += v * solve(k, n - 1)
        minimum = min(minimum, result)
    seen[code, n] = minimum
    return minimum


result = 0
for line in lines:
    best = 100000000000000000000000
    for a in solve_numpad(line):
        for aa in solve_dpad(a):
            best = min(best, solve(aa, 24))
    result += best * int(line.replace("A", ""))


# Part 2 = 191139369248202
print(f"answer = {result}")
assert result == 191139369248202
