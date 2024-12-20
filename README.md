# advent_of_code_24
https://adventofcode.com/2024

## Day 1
- Part 1: Sort the numbers then find the difference.
- Part 2: Count the number of occurances.

## Day 2
- Part 1: Calculate the diffs and then check they ascend or descend and the diffs are less than 4.
- Part 2: Remove one of the values before calculating the diff, then repeat part 1.

Very ugly. Can compare the data against sorted and reverse to check they are in order, then do the diff check afterwards.

## Day 3
- Part 1: Regex to find the digits.
- Part 2: Regex to find "do()", "don't()" and the digits.

## Day 4
- Part 1: Added padding around the data, so don't need to worry about edges. For every 'X' see if there is a 'MAS' in any direction. 
- Part 2: For every 'A' see if there is a 'MAS' on the two diagonals. 

## Day 5
- Part 1: Go through the updates and see if there are any rule violations.
- Part 2: On the invalid updates from part 1, find the first invalid ordering and swap the values, then repeat until valid.

## Day 6
- Part 1: Standard walking around algorithm.
- Part 2: First (slow) solution was to try putting a block in every possible position. Takes ~90 seconds with Pypy.

Only checking the spaces visited in part 1 brings it down to ~28 seconds.

Removing the deep copy brings it down to 3 seconds.

## Day 7
- Part 1: Build a (pruned) tree where the branches are either + or * the value. Don't add branches if the value exceeds the target.
- Part 2: Same but now with three branches as we have the "concat" operator.

## Day 8
- Part 1: Iterate over each pair of the same antennas to calculate the Manhattan distance, then add the resonances if they are within bounds.
- Part 2: Same as part 1 but for each antenna pair repeatedly add the Manhattan distance until the bounds are exceeded. Don't forget that the antennas themselves are a resonance!

## Day 9
- Part 1: Starting from the last file, squeeze each element into the gaps.
- Part 2: Starting from the last file, try to find a gap to put the whole file in. If a gap is found, then move it and then recalculate the gaps (brute force). Takes ~30 seconds with Python and ~3 seconds with Pypy.

If the file size and gap size are the same then don't need to brute force, just set the gap size to zero. Take ~3 seconds with Python.

Eliminate brute force completely results in ~2 seconds for Python.

## Day 10
- Part 1: Use a queue to keep track of the current position and move to each valid option (BFS). Sum the number of peaks visited.
- Part 2: Same but count the number of different ways of getting to a particular peak.

## Day 11
- Part 1: Simple brute force.
- Part 2: Wasted a lot of time trying to work out if there was a pattern before realising it was just a DP problem.

In fact, it is much much simpler than that: could just use two Counters! See code.

## Day 12
- Part 1: First map out the regions as the puzzle input can have separate regions with the same letter. For each region (a set), count the number of non-region squares surrounding the region to get the number of edges.
- Part 2: Similar to part 1 but for each edge, find the left-most or top-most edge (depending on orientation) that is part of the same side and add that to the set of edges. I needed to also store the direction of the edge because sometimes the same edge needs to be used twice.

```
AAAAAA
AAAA  <- the edge represented by the gap needs to be included twice as it represents two edges, top and bottom.
AAAAAA
```

## Day 13
- Part 1: Initially did it as a BFS but part 2 soon made it clear that solving it as an equation is better.
- Part 2: Same as part 1, but because the numbers are so big use a binary search to find the number that solves the equation.

Internet tip:
Cramer's rule makes it trival.

## Day 14
- Part 1: Use modulo to jump forward 100 seconds.
- Part 2: I assumed that for the tree that there would be no overlapping robots - it worked out!

Alternative but slower: calculate the safety vs time. When the tree appears the safety should be minimised as the tree is mostly in one quadrant, so the multiplication to calculate the safety would give a lower value (see code).

## Day 15:
- Part 1: Simple enough, when against a crate check for any empty spaces in the direction of the push, if found then shift everything along.
- Part 2: More complicated in the vertical direction as each crate can push up to others and this can cascade. Use recursion to see if a crate is valid to move by checking the crates it might push can be moved. Use brute force to clean up any unpaired `[`s or `]`s.

Had a bug where the same crate could be moved to a new position multiple times which messed up the `[` and `]`s pairings. Solution is not to move crates that have already moved this turn.

Swapping the crate with the spaces recursively starting from the bottom removes the occurance of unpaired `[`s and `]`s.
```
@.      @.      @.      @.
[]      []      []      ..
[]  =>  []  =>  ..  =>  []
[]      ..      []      []
..      []      []      []
```

## Day 16:
- Part 1: BFS to find the best route to the target.
- Part 2: Modify part 1 to keep track of each route as a set and collect all the best routes to the target. Finally, combine all the sets to get the total number of places on a best route to the target.

Runs in about 6 seconds with Python. It would be nice to make it a little quicker.

## Day 17:
- Part 1: Implemented the simple computer.
- Part 2: It would run for days, so I looked for a pattern. I noticed that the digits for the last output value repeats after 8 steps, and as more output digits are added each step repeats 8**n times before moving to the next value. The second to last value does something similar but 8**(n-1) and so on. That was enough to work out what was going on. See the code for a better description.

## Day 18:
- Part 1: For fun I did it like Conway's GoL. Might not be the most efficient but is quick enough.
- Part 2: BFS flood fill as new blocks are added. If the goal cannot be reached then we have our answer. Works but is slow (~44 seconds using Pypy).

Let's speed it up:
- Max heap brings it down to ~27 seconds.
- Use binary search brings it down to <1 second.

## Day 19:
- Part 1: Simple BFS initally.
- Part 2: BFS too slow, so switched to DP. Also, made it solve part 1 at the same time.
