'''
Integer or String
Description
You have been using ast.literal_eval() to take input in a suitable format. Have you thought of how does it distinguish between different data types and data structures? We will solve a similar but smaller problem here. You will be given a string as input. You just have to determine if the string can be an integer or no?
This is also encountered a lot in Data Science. Upon taking a lot of data, sometimes integer values are treated as a string, and due to that a lot of functionalities of integer data which you will learn ahead are rendered useless.

----------------------------------------------------------------------
Input:
A single line of string

Output:
INT if the input string is an integer and STR otherwise.

----------------------------------------------------------------------
Sample input:
12

Sample output:
INT

----------------------------------------------------------------------
Sample input:
12.4

Sample output:
STR

Explanation: You only have to print INT if its an integer, in this case, it is a float.

----------------------------------------------------------------------
Sample input:
43a

Sample output:
STR
'''
#inut has been taken for you
in_str=input().strip()

#find out if in_str is integer or not
def check_data_type(s):
    if s.isdigit() or (s[0] == '-' and s[1:].isdigit()):  # Checks for positive & negative integers
        return "INT"
    return "STR"

print(check_data_type(in_str))
