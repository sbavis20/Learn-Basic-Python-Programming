'''
Cheapest Item
Description
You will be given a dictionary with keys as items and values as their prices. You have to print the cheapest item.

----------------------------------------------------------------------
Sample input:
A single line non-empty dictionary

Sample output:
cheapest_item name: cheapest_item_cost

----------------------------------------------------------------------
Sample input:
{'mobile1':10000, 'mobile2':11000, 'mobile3':13000, 'mobile4':9000, 'mobile5':15000, 'mobile6':16000, 'mobile7':17000, 'mobile8':18000, 'mobile9':19000}

Sample output:
mobile4: 9000

'''
#take input here


#start writing your code here
import ast, sys

# Read input dictionary
input_str = sys.stdin.read()
items = ast.literal_eval(input_str)  # Convert string to dictionary

# Find the cheapest item (min by value, preserving order)
cheapest_item = min(items, key=items.get)

# Print result in required format
print(f"{cheapest_item}: {items[cheapest_item]}")
