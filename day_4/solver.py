import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

padded = [" " * (len(lines[0]) + 8) for _ in range(4)]

for l in lines:
    padded.append("    " + l + "    ")

padded.extend([" " * (len(lines[0]) + 8) for _ in range(4)])

funcs = [
    (lambda r, c, i: (r, c + i)),
    (lambda r, c, i: (r, c - i)),
    (lambda r, c, i: (r + i, c)),
    (lambda r, c, i: (r - i, c)),
    (lambda r, c, i: (r + i, c + i)),
    (lambda r, c, i: (r + i, c - i)),
    (lambda r, c, i: (r - i, c - i)),
    (lambda r, c, i: (r - i, c + i)),
]

result = 0

for r in range(len(padded[0])):
    for c in range(len(padded[0])):
        if padded[r][c] != "X":
            continue

        for f in funcs:
            letters = "X"
            for i in range(1, 4):
                rr, cc = f(r, c, i)
                letters += padded[rr][cc]
            if letters == "XMAS":
                result += 1


# Part 1 = 2532
print(f"answer = {result}")

result = 0

for r in range(len(padded[0])):
    for c in range(len(padded[0])):
        if padded[r][c] != "A":
            continue
        down = [padded[r - 1][c - 1], padded[r + 1][c + 1]]
        up = [padded[r + 1][c - 1], padded[r - 1][c + 1]]
        if sorted(down) == ["M", "S"] and sorted(up) == ["M", "S"]:
            result += 1

# Part 2 = 1941
print(f"answer = {result}")
