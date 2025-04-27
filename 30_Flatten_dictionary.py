'''
Flatten a dictionary
Description

Consider a nested dictionary as follows:

{'Fruit': 1, 'Vegetable': {'Cabbage': 2, 'Cauliflower': 3}, 'Spices': 4}

Your task is to flatten a nested dictionary and join the nested keys with the "_" character. For the above dictionary, the flattened dictionary would be as follows:

{'Fruit': 1, 'Vegetable_Cabbage': 2, 'Vegetable_Cauliflower': 3, 'Spices': 4}


The input will have a nested dictionary.

The output should have two lists. The first list will have keys and the second list should have values. Both lists should be sorted.

Sample Input:

{'Fruit': 1, 'Vegetable': {'Cabbage': 2, 'Cauliflower': 3}, 'Spices': 4}

Sample Output:

['Fruit', 'Spices', 'Vegetable_Cabbage', 'Vegetable_Cauliflower']
[1, 2, 3, 4]

'''

import ast, sys

# Read input
input_str = sys.stdin.read()
input_dict = dict(ast.literal_eval(input_str))

# Function to flatten a nested dictionary
def flatten_dict(dd, separator='_', prefix=''):
    flat_dict = {}

    for key, value in dd.items():
        new_key = f"{prefix}{separator}{key}" if prefix else key

        if isinstance(value, dict):  # If value is a nested dictionary, recurse
            flat_dict.update(flatten_dict(value, separator, new_key))
        else:
            flat_dict[new_key] = value  # Store flattened key-value pair

    return flat_dict

# Flatten the dictionary
flattened = flatten_dict(input_dict)

# Get sorted keys and values
out1 = sorted(flattened.keys())
out2 = sorted(flattened.values())

# Print outputs
print(out1)
print(out2)
