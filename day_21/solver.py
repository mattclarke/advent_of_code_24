import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]
print(lines)

num_pad = {
    "7":(0, 0) ,
   "8":(0, 1),
   "9":(0, 2),
   "4":(1, 0),
   "5":(1, 1),
   "6":(1, 2),
   "1":(2, 0),
   "2":(2, 1),
   "3":(2, 2),
   "":(3, 0) ,
   "0":(3, 1),
   "A":(3, 2),
}


dpad = {
    "" : (0,0),
    "^": (0,1),
    "A": (0,2),
    "<": (1,0),
    "v": (1,1),
    ">": (1,2),
}


def solve_numpad(code):
    current = "A"
    result = ""
    for c in code:
        curr = num_pad[current]
        nxt = num_pad[c]
        vdiff = curr[0] - nxt[0]
        hdiff = curr[1] - nxt[1]
        if vdiff > 0:
            result += "^"*vdiff
        elif vdiff < 0:
            result += "v"*abs(vdiff)
        if hdiff > 0:
            result += "<"*hdiff
        elif hdiff < 0:
            result += ">"*abs(hdiff)
        result +="A"
        current = c
    return result


def solve_dpad(code):
    current = "A"
    result = ""
    for c in code:
        curr = dpad[current]
        nxt = dpad[c]
        vdiff = curr[0] - nxt[0]
        hdiff = curr[1] - nxt[1]
        if vdiff > 0:
            result += "^"*vdiff
        elif vdiff < 0:
            result += "v"*abs(vdiff)
        if hdiff > 0:
            result += "<"*hdiff
        elif hdiff < 0:
            result += ">"*abs(hdiff)
        result +="A"
        current = c
    return result


result = 0
for line in lines:
    ans = solve_numpad(line)
    print(ans)
    ans = solve_dpad(ans)
    print(ans)
    print(len(ans))
    ans = solve_dpad(ans)
    print(len(ans))
    print(ans)
    result += len(ans) * int(line.replace("A", ""))

# Part 1 =
print(f"answer = {result}")

result = 0

# Part 2 =
print(f"answer = {result}")
