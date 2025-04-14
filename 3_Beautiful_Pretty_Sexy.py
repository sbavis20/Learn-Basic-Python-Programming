'''Beautiful Pretty Sexy
Description
A number k is beautiful if it is of the form 3n+1, is pretty if it is of the form 3n+2 and is sexy if it is of form 3n.
Given a number k, print if it is beautiful, pretty or sexy.

Sample input:
21

Sample output:
sexy

Sample input:
22

Sample output:
beautiful

Sample input:
23

Sample output:
pretty
'''
#input has been taken for you

k=int(input())

#check if the number is beautiful, pretty or sexy
#beautiful  3n+1, pretty 3n+2  sexy 3n.
reminder = k%3
#print(reminder)
if reminder==0:
    print('sexy')
elif reminder==1:
    print('beautiful')
elif reminder==2:
    print('pretty')
