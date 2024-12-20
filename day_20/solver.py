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


ref = find_ref(TRACK)


def solve(num_cheat, min_diff=0):
    results = []
    for (r, c), current in ref.items():
        Q = deque([((r, c), 0)])
        while Q:
            (rr, cc), n = Q.popleft()
            if n > num_cheat:
                continue
            if TRACK.get((rr, cc)) == ".":
                prev = ref[rr, cc]
                if prev > current:
                    diff = prev - current - n
                    if diff > min_diff - 1:
                        results.append(diff - n)

            # Look in all four directions + 1 to see if we can hit a short cut
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = rr + dr, cc + dc
                if n == 0 and TRACK.get((nr, nc)) != "#":
                    continue
                Q.append(((nr, nc), n + 1))
                # if TRACK.get((nr, nc)) != "#":
                #     continue
                # for i in range(1, num_cheat):
                #     nnr = nr + dr * i
                #     nnc = nc + dc * i
                #     if TRACK.get((nnr, nnc)) == ".":
                #         prev = ref[nnr, nnc]
                #         if prev > current:
                #             diff = prev - current
                #             results.append(diff - 2)
    return results


result = len(solve(2, 100))

# Part 1 = 1381
print(f"answer = {result}")

result = 0

# Part 2 =
print(f"answer = {result}")
