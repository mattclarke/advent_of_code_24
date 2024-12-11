import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line][0]
NUMBERS = [int(x) for x in lines.split(" ")]

numbers = NUMBERS[:]

for _ in range(25):
    new_numbers = []
    for n in numbers:
        sn = str(n)
        if n == 0:
            new_numbers.append(1)
        elif len(sn) % 2 == 0:
            half = len(sn) // 2
            a = sn[:half]
            b = sn[half:]
            new_numbers.append(int(a))
            new_numbers.append(int(b))
        else:
            new_numbers.append(n * 2024)
    numbers = new_numbers

# Part 1 = 194482
print(f"answer = {len(numbers)}")

result = 0

# Part 2 =
print(f"answer = {result}")
