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


def solve_1(robots, width, height, i=100):
    layout = {}
    for robot in robots:
        r, c, vr, vc = robot
        nr = (r + i * vr) % height
        nc = (c + i * vc) % width
        layout[nr, nc] = layout.get((nr, nc), 0) + 1
    quads = [0, 0, 0, 0]
    for r in range(height):
        for c in range(width):
            if r < height // 2 and c < width // 2:
                quads[0] += layout.get((r, c), 0)
            elif r < height // 2 and c > width // 2:
                quads[1] += layout.get((r, c), 0)
            elif r > height // 2 and c < width // 2:
                quads[2] += layout.get((r, c), 0)
            elif r > height // 2 and c > width // 2:
                quads[3] += layout.get((r, c), 0)
    return quads[0] * quads[1] * quads[2] * quads[3]


result = solve_1(robots[:], WIDTH, HEIGHT)


# Part 1 = 220971520
print(f"answer = {result}")


def solve_2(robots, width, height):
    for i in range(1000000000000000000000):
        layout = {}

        for robot in robots:
            r, c, vr, vc = robot
            nr = (r + i * vr) % height
            nc = (c + i * vc) % width
            layout[nr, nc] = layout.get((nr, nc), 0) + 1
        draw = True
        for v in layout.values():
            if v > 1:
                draw = False
        if not draw:
            continue
        for r in range(height):
            line = []
            for c in range(width):
                line.append(str(layout.get((r, c), ".")))
            print("".join(line))
        return i


result = solve_2(robots[:], WIDTH, HEIGHT)

# Part 2 = 6355
print(f"answer = {result}")


# For fun try measuring the safety vs time.
# The minimum safety should correspond to where the tree is
# because the tree reduces the spread across the quadrants
# so the power is less.
# E.g. if we have 12 bots spread equally across the quads
# the safety would be 3 * 3 * 3 * 3 = 81
# But if the bots are mostly grouped into one or two quads then
# 1 * 5 * 1 * 5 = 25
powers = []
for i in range(7000):
    powers.append(solve_1(robots[:], WIDTH, HEIGHT, i))
lowest = min(powers)
print(powers.index(lowest))
