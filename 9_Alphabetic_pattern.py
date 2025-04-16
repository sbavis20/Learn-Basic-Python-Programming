'''
Alphabetic patterns
Description
Given a positive integer 'n' less than or equal to 26, you are required to print the below pattern

Sample Input: 5

Sample Output :
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

Sample Input  : 3

Sample Output :
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

Please note that this question was asked in a Data Scientist interview.

'''

def alphabet_pattern(n):
    for i in range(n - 1, -n, -1):
        # row = [chr(97 + abs(j)) for j in range(n - 1, abs(i) - 1, -1)]
        # print("-".join(row).center(4 * n - 3, "-"))
        row = [chr(97 + j) for j in range(n - 1, abs(i) - 1, -1)]  # Create letter sequence
        print("-".join(row + row[-2::-1]).center(4 * n - 3, "-"))  # Mirror and center


# Example usage
n = int(input())
alphabet_pattern(n)
