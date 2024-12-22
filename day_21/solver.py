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
    "v<<A",
    "v<A",
    "<A",
    "vA",
    ">A",
    "^A",
    "v>A",
    "<<A",
    "^<A",
    ">^A",
    ">>^A",
    ">>A",
    "^>A",
    "A",
}


def solve_dpad(code, best=1000000000):
    current = "A"
    result = ""
    for c in code:
        if current == "A" and c == "<":
            result += "v<<"
        elif current == "A" and c == "v":
            result += "v<"
        elif current == "A" and c == "^":
            result += "<"
        elif current == "A" and c == ">":
            result += "v"

        elif current == "^" and c == "<":
            result += "v<"
        elif current == "^" and c == "v":
            result += "v"
        elif current == "^" and c == "A":
            result += ">"
        elif current == "^" and c == ">":
            result += "v>"

        elif current == ">" and c == "<":
            result += "<<"
        elif current == ">" and c == "v":
            result += "<"
        elif current == ">" and c == "A":
            result += "^"
        elif current == ">" and c == "^":
            result += "^<"

        elif current == "v" and c == "<":
            result += "<"
        elif current == "v" and c == "^":
            result += "^"
        elif current == "v" and c == "A":
            result += "^>"
        elif current == "v" and c == ">":
            result += ">"

        elif current == "<" and c == "v":
            result += ">"
        elif current == "<" and c == "^":
            result += ">^"
        elif current == "<" and c == "A":
            result += ">>^"
        elif current == "<" and c == ">":
            result += ">>"
        elif current == c:
            pass
        else:
            assert False, f"{current}, {c}"
        result += "A"
        current = c
    return result


result = 0
for line in lines:
    ans = solve_numpad(line)
    best = 1000000000000
    for aa in ans:
        a = aa
        for _ in range(2):
            a = solve_dpad(a)
        best = min(best, len(a))

    result += best * int(line.replace("A", ""))

# Part 1 = 156714
print(f"answer = {result}")


def fast(code, n, solutions):
    if n == -1:
        print(f"miss {code}")
        result = solve_dpad(code)
        solutions[0][code] = result
        return result
    poss = solutions[n]
    result = ""
    while code:
        # print("code", code, n)
        to_add = None
        for p in poss:
            if code.startswith(p):
                to_add = p
                break
        # print("to_add", to_add)
        # input()
        if not to_add:
            result += fast(code, n - 1, solutions)
            break
        else:
            result += poss[to_add]
            code = code[len(to_add) :]
    return result


solutions = {
    0: {},
    1: {},
}

for a in moves:
    t = solve_dpad(a)
    solutions[0][a] = t
    solutions[1][t] = solve_dpad(t)

# print(solutions)
#
# print(fast("v<<A>>^Av<A<A>>^AvAA^<A>A", 1, solutions))
# print(solve_dpad("v<<A>>^Av<A<A>>^AvAA^<A>A"))

result = 0
for line in lines:
    ans = solve_numpad(line)
    best = 1000000000000
    for aa in ans:
        a = aa
        for i in range(2):
            # print("a", a)
            if i == 0:
                a = solve_dpad(a)
            else:
                a = fast(a, i, solutions)
        best = min(best, len(a))

    result += best * int(line.replace("A", ""))

# result = 0
# for line in lines[:1]:
#     print(line)
#     ans = solve_numpad(line)
#     best = 1000000000000
#     for aa in "<>^v":
#         a = aa
#         print(a)
#         for _ in range(5):
#             a = solve_dpad(a)
#             print(a)
#         best = min(best, len(a))
#         print("=====")
#
#     result += best * int(line.replace("A", ""))
# print(solve_dpad(">>^A"))

# Part 2 =
print(f"answer = {result}")
