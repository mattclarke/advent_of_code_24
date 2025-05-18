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
- Part 2: It would run for days, so I looked for a pattern. I noticed that the digits for the last output value repeats after 8 steps, and as more output digits are added each step repeats 8^n times before moving to the next value. The second to last value does something similar but 8^(n-1) and so on. That was enough to work out what was going on. See the code for a better description.

Reverse engineering the code means my input program (2,4,1,3,7,5,0,3,1,5,4,4,5,5,3,0):
```
B = A % 8
B = B ^ 3
C = A // (2**B)   => A >> B
A = A // (2**3)   => A >> 3
B = B ^ 5
B = B ^ C
OUT B % 8
Repeat if A is not zero
```
Integer division by 2^n is equivalent to `>> n`.

B is initially the last 3 bits of A and A has those 3 bits popped off.
This means we can regenerate the original A by left shifting by 3 and ORing with B.

We know that the final value of A is 0 because it exits, so we can work backwards.
We also know that B is in the range 0 to 7 because `B = B ^ 3`.
```
For the last value (0) of our program
OUT B % 8 must be 0
So we can try all the possible values of B and see which ones (plural!) work.

Note: plural because multiple values of B could be a solution.

A = 0
B = A % 8 => 0
B = B ^ 3 => 3
C = A >> B => 0
A = A >> 3 => 0
B = B ^ 5 => 6
B = B ^ C => 6
OUT B % 8 => 6 (wrong!)
A == 0 => exit

So, A = 0 is not a possible solution.

Let's try another one:

A = 6
B = A % 9 => 6
B = B ^ 3 => 5
C = A >> B => 0
A = A >> 3 => 0
B = B ^ 5 => 0
B = B ^ C => 0
OUT B % 8 => 0 (correct!)
A == 0 => exit

A = 6 is a possible solution for getting the last output correct.
This means what when generating the previous output number (3) the final value of A must be 6.
```
See the code!

## Day 18:
- Part 1: For fun I did it like Conway's GoL. Might not be the most efficient but is quick enough.
- Part 2: BFS flood fill as new blocks are added. If the goal cannot be reached then we have our answer. Works but is slow (~44 seconds using Pypy).

Let's speed it up:
- Max heap brings it down to ~27 seconds.
- Use binary search brings it down to <1 second.

## Day 19:
- Part 1: Simple BFS initally.
- Part 2: BFS too slow, so switched to DP. Also, made it solve part 1 at the same time.

## Day 20:
- Part 1: As there is only one path and no branches, I first solve it with no cheats to get a reference value for each step. Then for every step along the route, find the positions reachable within the cheat limit. Calculate the new time based on the reference time difference for the current position and the positions reachable by cheating. If the new time is 100+ picoseconds quicker add 1 to the result.
- Part 2: Same but with a bigger cheat time.

## Day 21:
- Part 1: Implementing the algorithm. Didn't read the instructions correctly, so missed that the robot cannot pass through the blank square.
- Part 2: Took days to solve, not my finest effort. As the number of moves approximately double with each robot added it soon becomes too big. However, all the moves are constructed from a limited sets of sub-moves, so we just need to count the number of each sub-move in the move and then only recurse on each sub-move and multiple the result by the number of occurances. Finally, to make it fast use a cache.

I actually tried this solution earlier on but I must have made a mistake because I got the wrong answer. Reimplementing it from sratch on the 26th worked.

The mistake was that when calculating the d-pad, the order of, say, "^>" matters. If we change it to ">^" then we get the wrong answer! Using BFS to generate the d-pad would have caught this, so I added it back.

From the internet: why the order matters. Consider this example:
```
<^A (3)  ->  v<<A  >^A  >A (9)  ->  <vA<AA>>^A  vA<^A>A  vA^A (21)
^<A (3)  ->  <A  v<A  >>^A (9)  ->  v<<A>>^A  <vA<A>>^A  vAA<^A>A (25)
```
It shows that "<^A" is shorter than "^<A".

To generalise, each left step from A is more expensive for the next robot, so we should always do the < key first, then the ^ or v key, then the > key (where the rules permit). E.g. "<^" not "^<", "^>" not ">^", and so on.

## Day 22:
- Part 1: Simple - just a test that one has entered the algorithm correctly.
- Part 2: As it is pseudo-random and the maximum number of values possible is 16777216 due to the "prune", I decided to calculate all the values for one of the seeds (the reference seed). For the remaining seeds, I only need to calculate the first value and then find its index relative to the same value in the reference seed to get an offset. For the first 2000 values of the reference make a rolling window of the differences and look for the same pattern relative to the offsets. If it matches add the corresponding value.

Slow at ~30s for Pypy and feels a bit brute force. Afterwards, I tried a true brute force solution which didn't finish before I gave up after a minute or two.

Internet solution: during part 1, track the last four differences and if they haven't been seen before add them to the total for that difference pattern. To get the answer, find the maximum total.

## Day 23:
- Part 1: Build the graph and collect the tees. For the tees, find the the groups of three using three nested loops.
- Part 2: Loop through all the node. For each one, give all the nodes it connects to a score of 1, then for each of those nodes do the same. The starting node will have the largest score but the biggest group (not including the starting node) will have a score of the largest minus 1.

This was a bit of a fluke, it only works because each node has the same number of connections and the most number of connections is one less than the total number of connections.

A more general solution is create sets for each node and look for repetitions of sets. If there is a repetition of a set equal to the length of the set minus one, then that is a group where all are connected to each other. Just need to find the biggest group.

There is also the Bron-Kerbosch algorithm for finding "cliques". See the code for an example.

## Day 24:
- Part 1: Testing that the algorithm was implemented correctly
- Part 2: First solved it by hand!

Now done in code! 
- Set all bits of X to 1 and Y to 0 then run the algorithm. 
- Find the least significant 0 in the answer and start swapping outputs until that is fixed
- Then check some random additions, if they pass recurse. If they don't pass then backtrack.

Code is ugly and slow (~30s), but I've had enough for now!
One possible speed up is to build a graph of the non-Z outputs, then it will be possible to check whether an output is relevant to the current Z thus reducing the values we need to consider when swapping.
E.g. for z09, rkf depends on x08, y08, x09, y09, x07 and y07, so is worth trying to swap.

## Day 25:
- Part 1: Simple!
- Part 2: No part 2 as usual!
