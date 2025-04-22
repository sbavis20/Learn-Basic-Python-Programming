'''
Find Extra Character
Description
Given two strings, one of the strings will contain an extra character. Find the extra character. The number of all the other characters in both the strings will be the same. Check the sample input/output for more clarification.

The code will be case sensitive.

----------------------------------------------------------------------
Input:
Two strings on two separate lines.

Output:
One Character which is extra in one of the strings

----------------------------------------------------------------------
Sample input:
abcd
cedab

Sample output:
e

'''
#take input on your own
str1 = input().strip()
str2 = input().strip()

#write code to find the extra character here
def find_extra_character(str1, str2):
    char_count = {}

    # Count characters in str2
    for char in str2:
        char_count[char] = char_count.get(char, 0) + 1

    # Subtract counts using str1
    for char in str1:
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]

    # The remaining key in char_count is the extra character
    return list(char_count.keys())[0]

print(find_extra_character(str1, str2))
