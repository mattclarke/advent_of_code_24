import copy
import sys
from collections import deque, defaultdict


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

layout = defaultdict(set)
tees = set()

for line in lines:
    a, b = line.split("-")
    layout[a].add(b)
    layout[b].add(a)
    if a.startswith("t"):
        tees.add(a)
    if b.startswith("t"):
        tees.add(b)

contains_t = set()

for t in tees:
    nodes = layout[t]
    for n in nodes:
        for nn in layout[n]:
            if n == nn or nn == t:
                continue
            if t in layout[nn]:
                contains_t.add(frozenset({t, n, nn}))

# Part 1 = 1218
print(f"answer = {len(contains_t)}")

result = []

for n, nodes in layout.items():
    scores = {}
    for nn in nodes:
        scores[nn] = scores.get(nn, 0) + 1
        conns = layout[nn]
        for nnn in layout[nn]:
            scores[nnn] = scores.get(nnn, 0) + 1
    ans = [n]
    for k, v in scores.items():
        if v == scores[n] - 1:
            ans.append(k)
    if len(ans) > len(result):
        result = sorted(ans)

# Part 2 = ah,ap,ek,fj,fr,jt,ka,ln,me,mp,qa,ql,zg
print(f"answer = {','.join(result)}")
