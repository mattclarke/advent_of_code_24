import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

result = 0

TRACK = {}
START = None
END = None
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == "S":
            START = (r, c)
            TRACK[r, c] = "."
        elif ch == "E":
            END = (r, c)
            TRACK[r, c] = "."
        else:
            TRACK[r, c] = ch


def find(track, can_cheat, limit=1000000):
    Q = deque([(START, 0, can_cheat, set(), False)])
    solution = []

    while Q:
        (r, c), steps, can_cheat, seen, is_cheating = Q.popleft()
        if steps > limit:
            continue
        if (r, c) == END:
            solution.append(steps)
            break
        seen.add((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr = r + dr
            nc = c + dc
            if (nr, nc) in seen:
                continue
            if can_cheat and track.get((nr, nc)) == "#":
                # Start cheating
                Q.append(((nr, nc), steps + 1, False, copy.copy(seen), True))
            if track.get((nr, nc)) == ".":
                # Normal move
                Q.append(((nr, nc), steps + 1, can_cheat, copy.copy(seen), False))
    return solution


normal = find(TRACK, False)[0]
# print(normal)
# ans = find(TRACK, True, normal)
# print([normal -x for x in ans if x != normal])
# print(len([normal -x for x in ans if x != normal]))

count = 0

for r in range(1, len(lines) - 1):
    for c in range(1, len(lines[0])-1):
        horiz = TRACK[r,c] == "#" and TRACK[r, c-1] == "." and TRACK[r, c+1] == "."
        vert = TRACK[r,c] == "#" and TRACK[r-1, c] == "." and TRACK[r+1, c] == "."
        if horiz or vert:
            track = copy.copy(TRACK)
            track[r,c] = "."
            ans = find(track, False, normal)
            count+=1
            print(count, normal - ans[0], ans[0])

        


# Part 1 =
print(f"answer = {result}")

result = 0

# Part 2 =
print(f"answer = {result}")
