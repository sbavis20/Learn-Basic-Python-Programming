'''
Maximum Distance
Description
You will be given a list of repeated elements. You have to find the maximum distance between two same elements. The answer will be zero if there are no repeated elements.

----------------------------------------------------------------------
Input:
A non-empty list of integers.

Output:
A single integer denoting the maximum distance between two same integers.

----------------------------------------------------------------------
Sample input:
[1, 2, 3, 2, 5, 1, 2, 4, 6, 2, 7, 8, 6]

Sample output:
8

Explanation:
Max distance for 1: 5
Max distance for 2: 8
Max distance for 3: 0
Max distance for 4: 0
Max distance for 5: 0
Max distance for 6: 4
Max distance for 7: 0
Max distance for 8: 0

'''
import ast

# Read input list
input_list = ast.literal_eval(input())

def max_distance(lst):
    index_map = {}  # Dictionary to store first occurrence of each number
    max_dist = 0  # Variable to track the maximum distance

    for i, num in enumerate(lst):
        if num in index_map:
            max_dist = max(max_dist, i - index_map[num])  # Update max distance
        else:
            index_map[num] = i  # Store the first occurrence

    return max_dist

# Output the maximum distance
print(max_distance(input_list))
