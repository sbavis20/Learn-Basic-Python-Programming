'''
Reverse The Digits
Description
You will be given a number. You have to reverse the digits of the number and print it.

----------------------------------------------------------------------
Input:
A positive integer greater than zero

Output:
The number in reverse order. Check sample outputs for more details.

----------------------------------------------------------------------
Sample input:
345200

Sample output:
2543

----------------------------------------------------------------------
Sample input:
6752343

Sample output:
3432576
'''
#take input of the number here
number = int(input())

#write code to reverse the number here
def reverse(n):
    my_rev=[]
    temp=0
    length = len(str(n))
    for i in range(length):
        temp=n%10
        my_rev.append(temp)
        n=int(n/10)
        #print(n)
    string_list_1 = "".join(map(str, my_rev))
    print(string_list_1 )
# r = number
# print(reverse(r))
reverse(number)
