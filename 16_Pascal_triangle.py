'''
Pascal's Triangle
Description
A pascal's triangle is a very interesting mathematical concept.
Each number here is a sum of the two numbers directly above it.
Following is an 8 level Pascal's triangle:﻿
﻿
You can read about Pascal's triangle here.
Your task is to print an nth level of Pascal's triangle.
The input will contain an integer n.
The output will contain 1 line of the list of numbers representing the nth row of Pascal's triangle.

Sample Input:
6
Sample Output:

[1, 5, 10, 10, 5, 1]
'''

#input has been taken for you
n = int(input())
row = [1]  # First element is always 1

for k in range(1, n):
    row.append(row[-1] * (n - k) // k)  # Compute next value using nCr formula

print(row)




