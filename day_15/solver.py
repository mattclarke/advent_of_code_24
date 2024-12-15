import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n\n") if line]
LAYOUT = {}

MOVES = lines[1].replace("\n", "")
START = None

for r, l in enumerate(lines[0].split("\n")):
    for c, ch in enumerate(l):
        if ch == "@":
            START = (r, c)
            ch = "."
        LAYOUT[r, c] = ch
R = len(lines[0].split("\n"))
C = len(lines[0].split("\n")[0])


def pprint(layout, pos):
    for rr in range(R):
        line = []
        for cc in range(C):
            if (rr, cc) == pos:
                line.append("@")
            else:
                line.append(layout[rr, cc])
        print("".join(line))
    print("")


pos = START
layout = copy.deepcopy(LAYOUT)

for m in MOVES:
    r, c = pos
    if m == "<":
        dr, dc = 0, -1
    elif m == ">":
        dr, dc = 0, 1
    elif m == "^":
        dr, dc = -1, 0
    else:
        dr, dc = 1, 0
    if layout[r + dr, c + dc] == "#":
        pass
    elif layout[r + dr, c + dc] == ".":
        pos = (r + dr, c + dc)
    else:
        # Crate
        gap = None
        loc = (r + dr, c + dc)
        while True:
            if layout[loc] == ".":
                gap = loc
                break
            elif layout[loc] == "#":
                break
            else:
                loc = (loc[0] + dr, loc[1] + dc)
        if gap:
            pos = (r + dr, c + dc)
            layout[r + dr, c + dc] = "."
            layout[loc] = "O"

    # pprint(layout, pos)


result = 0
for r in range(R):
    for c in range(C):
        if layout[r, c] == "O":
            result += 100 * r + c


# Part 1 = 1463715
print(f"answer = {result}")

LAYOUT = {}
R = 0
C = 0
r = 0
START = None

for l in lines[0].split("\n"):
    c = 0
    for ch in l:
        if ch == "@":
            START = (r, c)
            LAYOUT[r, c] = "."
            LAYOUT[r, c + 1] = "."
        elif ch == ".":
            LAYOUT[r, c] = "."
            LAYOUT[r, c + 1] = "."
        elif ch == "#":
            LAYOUT[r, c] = "#"
            LAYOUT[r, c + 1] = "#"
        elif ch == "O":
            LAYOUT[r, c] = "["
            LAYOUT[r, c + 1] = "]"
        c += 2
        C = max(C, c)
    r += 1
    R = max(R, r)


def can_move_up(layout, pos, clayout):
    moved = set()

    def _do(layout, pos, clayout):
        r, c = pos
        if layout[pos] == "#":
            return False
        if layout[pos] == ".":
            return True
        if layout[pos] == "]":
            c -= 1

        if layout[r, c] == "[":
            result = _do(layout, (r - 1, c), clayout) and _do(
                layout, (r - 1, c + 1), clayout
            )
            if result:
                if (r, c) not in moved:
                    clayout[r - 1, c] = clayout[r, c]
                    moved.add((r, c))
                if (r, c + 1) not in moved:
                    clayout[r - 1, c + 1] = clayout[r, c + 1]
                    moved.add((r, c + 1))
            return result
        else:
            assert False, "can move up"

    return _do(layout, pos, clayout)


def can_move_down(layout, pos, clayout):
    moved = set()

    def _do(layout, pos, clayout):
        r, c = pos
        if layout[pos] == "#":
            return False
        if layout[pos] == ".":
            return True
        if layout[pos] == "]":
            c -= 1

        if layout[r, c] == "[":
            result = _do(layout, (r + 1, c), clayout) and _do(
                layout, (r + 1, c + 1), clayout
            )
            if result:
                if (r, c) not in moved:
                    clayout[r + 1, c] = clayout[r, c]
                    moved.add((r, c))
                if (r, c + 1) not in moved:
                    clayout[r + 1, c + 1] = clayout[r, c + 1]
                    moved.add((r, c + 1))
            return result
        else:
            assert False, "can move down"

    return _do(layout, pos, clayout)


layout = copy.deepcopy(LAYOUT)

pos = START
for nim, m in enumerate(MOVES):
    # if nim > 0:
    #     pprint(layout, pos)
    #     input(f"{nim}, {m}")
    r, c = pos
    if m == "<":
        dr, dc = 0, -1
    elif m == ">":
        dr, dc = 0, 1
    elif m == "^":
        dr, dc = -1, 0
    else:
        dr, dc = 1, 0
    if layout[r + dr, c + dc] == "#":
        continue
    elif layout[r + dr, c + dc] == ".":
        pos = (r + dr, c + dc)
    else:
        # Crate
        if dc == -1:
            gap = None
            loc = (r, c + dc)
            while True:
                if layout[loc] == ".":
                    gap = loc
                    break
                elif layout[loc] == "#":
                    break
                else:
                    loc = (loc[0], loc[1] + dc)
            if gap:
                # Shift left
                for nc in range(loc[1], c):
                    layout[r, nc] = layout[r, nc + 1]
                pos = (r, c + dc)
        elif dc == 1:
            gap = None
            loc = (r, c + dc)
            while True:
                if layout[loc] == ".":
                    gap = loc
                    break
                elif layout[loc] == "#":
                    break
                else:
                    loc = (loc[0], loc[1] + dc)
            if gap:
                # Shift right
                for nc in range(loc[1], c, -1):
                    layout[r, nc] = layout[r, nc - 1]
                pos = (r, c + dc)
        elif dr == -1:
            clayout = copy.copy(layout)
            can = can_move_up(layout, (r + dr, c), clayout)
            if can:
                layout = clayout
                pos = (r + dr, c)
        elif dr == 1:
            clayout = copy.copy(layout)
            can = can_move_down(layout, (r + dr, c), clayout)
            if can:
                layout = clayout
                pos = (r + dr, c)
        layout[pos] = "."
        # Clean up
        for rr in range(R):
            for cc in range(C):
                if layout[rr, cc] == "[" and layout[rr, cc + 1] != "]":
                    layout[rr, cc] = "."
                elif layout[rr, cc] == "]" and layout[rr, cc - 1] != "[":
                    layout[rr, cc] = "."
pprint(layout, pos)
for r in range(R):
    for c in range(C):
        if layout[r, c] == "#" and LAYOUT[r, c] != "#":
            print("oops", r, c)
            input()


result = 0
for r in range(R):
    for c in range(C):
        if layout[r, c] == "[":
            result += 100 * r + c

# Part 2 = 1481392
print(f"answer = {result}")
