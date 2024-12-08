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
