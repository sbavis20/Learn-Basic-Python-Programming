'''
Vote for Food
Description
Your team is going for camping and you are taking a vote to decide what food to pack for dinner.
Everyone gets a vote and the food item that gets at least one more than half of the votes wins. None of the items wins if nothing gets at least one more than half votes. Assume that every person gets only one vote.
The input will contain a list of food items where each occurrence of an item represents one vote. You should print the winning food item as output. If there is no clear winner, print "NOTA".

Sample Input:
["pasta","pasta","pasta","pasta","pasta","paratha","paratha","paratha"]
Sample Output:
pasta
'''
import ast, sys
from collections import Counter

# Read input list
input_str = sys.stdin.read()
votes = ast.literal_eval(input_str)

def find_winner(votes):
    vote_count = Counter(votes)  # Count occurrences of each food item
    majority = len(votes) // 2  # More than half votes needed to win

    for food, count in vote_count.items():
        if count > majority:
            return food

    return "NOTA"  # No clear winner

# Output the winning food item
print(find_winner(votes))
