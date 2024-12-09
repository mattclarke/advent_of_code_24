import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

data = [int(ch) for ch in PUZZLE_INPUT.strip()]

processed = []
is_file = True
file_id = 0
gaps = []
nums = []
gaps_start = []  # Part2
gap_sizes = []  # Part2
files_start = []  # Part2
file_sizes = []  # Part2

for i in range(len(data)):
    if is_file:
        v = file_id
        file_id += 1
        is_file = False
        if data[i] != 0:
            files_start.append(len(processed))
            file_sizes.append(data[i])
    else:
        v = "."
        is_file = True
        if data[i] != 0:
            gaps_start.append(len(processed))
            gap_sizes.append(data[i])

    for r in range(data[i]):
        processed.append(v)
        if v == ".":
            gaps.append(len(processed) - 1)
        else:
            nums.append(len(processed) - 1)

processed_1 = processed[:]

while nums[~0] > gaps[0]:
    if not nums:
        break
    g = gaps.pop(0)
    n = nums.pop(~0)
    processed_1[g], processed_1[n] = processed_1[n], processed_1[g]

result = 0
for i, c in enumerate(processed_1):
    if c == ".":
        break
    result += i * c

# Part 1 = 6330095022244
print(f"answer = {result}")

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
        # Adjust gaps
        if gs == s:
            # Perfect fit
            gap_sizes[gi] = 0
        else:
            gaps_start[gi] = g + s
            gap_sizes[gi] = gs - s
            continue

result = 0
for i, c in enumerate(processed):
    if c == ".":
        continue
    result += i * c

# Part 2 = 6359491814941
print(f"answer = {result}")
