import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [int(ch) for ch in PUZZLE_INPUT.strip()]

result = 0
processed = []
is_file = True
file_id = 0
gaps = []
nums = []
i = 0

while i < len(lines):
    if is_file:
        v = file_id
        file_id += 1
        is_file = False
    else:
        v = "."
        is_file = True

    for r in range(lines[i]):
        processed.append(v)
        if v == ".":
            gaps.append(len(processed) - 1)
        else:
            nums.append(len(processed) - 1)
    i += 1

while nums[~0] > gaps[0]:
    if not nums:
        break
    g = gaps.pop(0)
    n = nums.pop(~0)
    processed[g], processed[n] = processed[n], processed[g]

for i, c in enumerate(processed):
    if c == ".":
        break
    result += i * c

# Part 1 = 6330095022244
print(f"answer = {result}")

result = 0
processed = []
is_file = True
file_id = 0
gaps_start = []
gap_sizes = []
files_start = []
file_sizes = []

i = 0

while i < len(lines):
    if is_file:
        v = file_id
        file_id += 1
        is_file = False
        if lines[i] != 0:
            files_start.append(len(processed))
            file_sizes.append(lines[i])
    else:
        v = "."
        is_file = True
        if lines[i] != 0:
            gaps_start.append(len(processed))
            gap_sizes.append(lines[i])

    for r in range(lines[i]):
        processed.append(v)
    nums = []
    i += 1

for n, s in zip(reversed(files_start), reversed(file_sizes)):
    gi = -1
    for i, gs in enumerate(gap_sizes):
        if gs >= s:
            gi = i
            break
    if gi >= 0 and gaps_start[gi] < n:
        gs = gap_sizes[gi]
        g = gaps_start[gi]
        for i in range(s):
            processed[g + i], processed[n + i] = processed[n + i], "."
        # Recalculate the gaps via brute force
        gaps_start.clear()
        gap_sizes.clear()
        in_gap = False
        gstart = 0
        for p in range(len(processed)):
            if processed[p] == ".":
                if not in_gap:
                    in_gap = True
                    gstart = p
            else:
                if in_gap:
                    gaps_start.append(gstart)
                    gap_sizes.append(p - gstart)
                    in_gap = False

for i, c in enumerate(processed):
    if c == ".":
        continue
    result += i * c

# Part 2 = 6359491814941
print(f"answer = {result}")
