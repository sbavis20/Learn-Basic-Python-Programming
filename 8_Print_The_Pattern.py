'''
Print The Pattern
Description
Printing different patterns is a very good exercise to reinforce iteration through loops and strong logic building. Here you will be given a positive integer and you will generate pattern based on that integer.

----------------------------------------------------------------------
Input:
A positive integer n
1 <= n <=20

Output:
A pattern as described by the Sample input and outputs below.

----------------------------------------------------------------------
Sample input:
5

Sample output:

    *
   *_*
  *_*_*
 *_*_*_*
*_*_*_*_*
'''

n = int(input())

for i in range(1,n+1):
	for j in range(n-i):
		print(' ',end='')
	for k in range(i-1):
		print('*_',end='')
	print('*')
