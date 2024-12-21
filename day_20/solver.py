import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

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


def find_ref(track):
    Q = deque([(START, 0)])
    seen = {}

    while Q:
        (r, c), steps = Q.popleft()
        if steps >= seen.get((r, c), 100000000):
            continue
        seen[r, c] = steps
        if (r, c) == END:
            return seen
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr = r + dr
            nc = c + dc
            if track.get((nr, nc)) == ".":
                Q.append(((nr, nc), steps + 1))

    assert False, "no solution"


def pprint(seen):
    for r in range(len(lines)):
        line = []
        for c in range(len(lines[0])):
            if TRACK[r, c] != "#" and (r, c) in seen:
                line.append(str(seen[r, c]))
            else:
                line.append(TRACK[r, c])
        print("".join(line))
    input()


def solve(num_cheat, min_diff=0):
    results = {}
    for (r, c), current in ref.items():
        Q = deque([((r, c), 0)])
        seen = {}
        while Q:
            (rr, cc), n = Q.popleft()
            if n > num_cheat:
                continue
            if (rr, cc) not in TRACK:
                continue
            if n >= seen.get((rr, cc), 1000000000):
                continue
            seen[(rr, cc)] = n

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = rr + dr, cc + dc
                Q.append(((nr, nc), n + 1))
        # pprint(seen)
        for (rr, cc), n in seen.items():
            if TRACK[rr, cc] == "#":
                continue
            if (rr, cc) == (r, c):
                continue
            value = ref[rr, cc]
            curr = ref[r, c]
            if value < curr:
                continue
            if curr + n >= value:
                continue
            savings = value - current - n
            if savings < min_diff:
                continue
            results[savings] = results.get(savings, 0) + 1

    return results


ref = find_ref(TRACK)

results = solve(2, 100)
result = sum(results.values())

# Part 1 = 1381
print(f"answer = {result}")

results = solve(20, 100)
result = sum(results.values())

# Part 2 = 982124
print(f"answer = {result}")
