import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]
print(lines)

num_pad = {
    (0, 0): "7",
    (0, 1): "8",
    (0, 2): "9",
    (1, 0): "4",
    (1, 1): "5",
    (1, 2): "6",
    (2, 0): "1",
    (2, 1): "2",
    (2, 2): "3",
    (3, 0): "",
    (3, 1): "0",
    (3, 2): "A",
}


def solve_numpad(code):
    Q = deque([(3, 2, 0, (), [])])
    result = []
    while Q:
        r, c, s, n, route = Q.popleft()
        if s >= 5:
            continue
        if num_pad[r, c] == code[len(n)]:
            # press it
            route += "A"
            t = list(n)
            t.append(num_pad[r, c])
            n = tuple(t)
            s = 0
        if len(n) == len(code):
            if "".join(n) == code:
                # complete
                result.append("".join(route))
            continue

        for d in ["^", "<", "v", ">"]:
            route_ = route[:]
            route_.append(d)
            if d == "^":
                if (r - 1, c) in num_pad:
                    Q.append((r - 1, c, s + 1, n, route_))
            elif d == "<":
                if (r, c - 1) in num_pad:
                    Q.append((r, c - 1, s + 1, n, route_))
            elif d == "v":
                if (r + 1, c) in num_pad:
                    Q.append((r + 1, c, s + 1, n, route_))
            elif d == ">":
                if (r, c + 1) in num_pad:
                    Q.append((r, c + 1, s + 1, n, route_))
    return result


result = solve_numpad("029A")
result.sort(key=lambda s: len(s))
lowest = len(result[0])
result = [x for x in result if len(x) == lowest]

# Part 1 =
print(f"answer = {result}")

result = 0

# Part 2 =
print(f"answer = {result}")
