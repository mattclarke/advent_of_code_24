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

result = set()

for n, nodes in layout.items():
    scores = defaultdict(set)
    for nn in nodes:
        scores[nn].add(n)
        scores[nn].add(nn)
        conns = layout[nn]
        for nnn in layout[nn]:
            if nnn in nodes:
                scores[nnn].add(nn)

    for k, s in scores.items():
        count = 0
        for kk, ss in scores.items():
            if s == ss:
                count += 1
        if count == len(s) - 1 and len(s) > len(result):
            result = s

# Part 2 = ah,ap,ek,fj,fr,jt,ka,ln,me,mp,qa,ql,zg
print(f"answer = {','.join(sorted(result))}")


def bron_kerbosch(layout, P, R, X, cliques, depth=0):
    # Finds the maximal cliques.
    # I.e. if A, B, C are in a clique then it returns {A, B, C} and skips {A, B}, etc.
    # P = prospective nodes
    # R = current clique
    # X = nodes already processed (avoids getting the same clique multiple times)
    # print(P, R, X, depth)
    if not P and not X:
        cliques.append(R)
        return
    while P:
        v = P.pop()
        bron_kerbosch(
            layout,
            P.intersection(layout[v]),
            R.union([v]),
            X.intersection(layout[v]),
            cliques,
            depth + 1,
        )
        X.add(v)


cliques = []
bron_kerbosch(layout, set(layout.keys()), set(), set(), cliques)
print(cliques)
