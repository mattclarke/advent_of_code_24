import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

rules, updates = PUZZLE_INPUT.split("\n\n")

rules = [line.strip() for line in rules.split("\n") if line]
updates = [line.strip() for line in updates.split("\n") if line]

result = 0

rules_dict = {}

for r in rules:
    f, s = r.split("|")
    f = int(f)
    s = int(s)
    # Insert values that aren't allowed before
    sr = rules_dict.get(s, set())
    sr.add(f)
    rules_dict[s] = sr

invalid = []

for n, up in enumerate(updates):
    values = [int(x) for x in up.split(",")]
    valid = True
    for i in range(len(values) - 1):
        curr = values[i]
        nxt = values[i + 1]
        if nxt in rules_dict[curr]:
            invalid.append(n)
            valid = False
            break
    if valid:
        result += values[len(values) // 2]

# Part 1 = 4959
print(f"answer = {result}")

result = 0

for n in invalid:
    values = [int(x) for x in updates[n].split(",")]
    new_order = values[:]
    while True:
        valid = True
        for i in range(len(values) - 1):
            curr = values[i]
            nxt = values[i + 1]
            if nxt in rules_dict[curr]:
                # Swap the invalid values
                new_order = values[:]
                new_order[i] = values[i + 1]
                new_order[i + 1] = values[i]
                valid = False
                break
        values = new_order[:]
        if valid:
            result += values[len(values) // 2]
            break

# Part 2 = 4655
print(f"answer = {result}")
