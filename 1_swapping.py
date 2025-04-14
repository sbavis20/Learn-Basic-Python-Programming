'''###Swapping
Description
You are given two integer variables,  x and y. You have to swap the values stored in x and y.

----------------------------------------------------------------------
Input:
Two numbers x and y separated by a comma.

Output:
Print 5 lines. The first two lines will have values of variables shown before swapping, and the last two lines will have values of variables shown after swapping. The third line will be blank.

----------------------------------------------------------------------
Sample input:
20, 50

Sample output:

x before swapping: 20
y before swapping: 50

x after swapping: 50
y after swapping: 20 ###'''

#Take input using input()

#input() takes input in form of the string
in_string=input()

#here extract the two numbers from the string
my_list = in_string.split(',')
x = int(my_list[0])
y = int(my_list[1])
#print x and y before swapping
print('x before swapping: {0}'.format(x))
print('y before swapping: {0}'.format(y))

#Writing your swapping code here
z = x
x = y
y = z


#print x and y after swapping
print()
print('x after swapping: {0}'.format(x))
print('y after swapping: {0}'.format(y))
