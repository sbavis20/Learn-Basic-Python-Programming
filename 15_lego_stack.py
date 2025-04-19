'''
Lego Stack
Description
You are given a row of Lego Blocks consisting of n blocks. All the blocks given have a square base whose side length is known. You need to stack the blocks over each other and create a vertical tower. Block-1 can go over Block-2 only if sideLength(Block-2)=>sideLength(Block-1).
From the row of Lego blocks, you on only pick up either the leftmost or rightmost block.
Print "Possible" if it is possible to stack all n cubes this way or else print "Impossible".

Input Format:
The input will contain a list of n integers representing the side length of each block's base in the row starting from the leftmost.

Sample Input:
[5 ,4, 2, 1, 4 ,5]
Sample Output:
Possible
'''
import ast, sys

# Read input
input_str = sys.stdin.read()
sides = ast.literal_eval(input_str)  # Convert input string to list

def can_stack_blocks(sides):
    max_block = float('inf')  # Start with an infinitely large block

    while sides:
        # Choose the larger of the two possible picks (leftmost or rightmost)
        if sides[0] >= sides[-1]:
            current_block = sides.pop(0)  # Pick from left
        else:
            current_block = sides.pop(-1)  # Pick from right

        # If the picked block is larger than the previous block, it's not stackable
        if current_block > max_block:
            return "Impossible"

        max_block = current_block  # Update the max_block with the picked block

    return "Possible"

# Print the result
print(can_stack_blocks(sides))
