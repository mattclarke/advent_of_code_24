import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
if len(sys.argv) > 1:
    WIDTH = 11
    HEIGHT = 7
else:
    WIDTH = 101
    HEIGHT = 103

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

robots = []

for l in lines:
    nums = l.replace("p=", "").replace(" v=", ",").split(",")
    c, r, vc, vr = [int(x) for x in nums]
    robots.append((r, c, vr, vc))


def solve_1(robots, width, height):
    layout = {}
    for robot in robots:
        r, c, vr, vc = robot
        nr = (r + 100 * vr) % height
        nc = (c + 100 * vc) % width
        layout[nr, nc] = layout.get((nr, nc), 0) + 1
    # for r in range(height):
    #     line = []
    #     for c in range(width):
    #         line.append(str(layout.get((r,c), ".")))
    #     print("".join(line))
    tl = 0
    tr = 0
    bl = 0
    br = 0
    for r in range(height):
        for c in range(width):
            if r < height // 2 and c < width // 2:
                tl += layout.get((r, c), 0)
            elif r < height // 2 and c > width // 2:
                tr += layout.get((r, c), 0)
            elif r > height // 2 and c < width // 2:
                bl += layout.get((r, c), 0)
            elif r > height // 2 and c > width // 2:
                br += layout.get((r, c), 0)
    return tl * tr * bl * br


result = solve_1(robots[:], WIDTH, HEIGHT)


# Part 1 = 220971520
print(f"answer = {result}")

result = 0

# Part 2 =
print(f"answer = {result}")
