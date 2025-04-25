'''
Balanced Brackets
Description
You will be given a string with a lot of brackets. You have to print if the brackets are balanced or not. Remember, there are three types of brackets: ‘( )’,  ‘{ }’ and ‘[ ]’.

----------------------------------------------------------------------
Input:
A string

Output:
Yes, if the brackets are balanced.
No otherwise.

----------------------------------------------------------------------
Sample input:
){[[]]}())()

Sample output:

No


----------------------------------------------------------------------
Sample input 2:
[](){[]()(){}}

Sample output 2:

Yes

'''
#take input
inp=input()
stack = []

for i in inp:
	if len(stack)==0:
		stack.append(i)
	else:
		if(i==')' and stack[-1]=='('):
			stack.pop()
		elif(i=='}' and stack[-1]=='{'):
			stack.pop()
		elif(i==']' and stack[-1]=='['):
			stack.pop()
		else:
			stack.append(i)

if stack:
	print('No')
else:
	print('Yes')
