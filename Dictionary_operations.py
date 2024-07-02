# Define a list of dictionaries, each dictionary containing word-description pairs
word_m = [
    {'Biscuit': 'Which you eat', 'apple': 'which you eat', 'tiger': 'which is animal',
     'Lion': 'which is king', 'Leopard': 'which runs', 'Banana': 'which gives calcium',
     'Tortoise': 'which is slow', 'Parrot': 'which talks a lot', 'eagle': 'which is silent',
     'Gym': 'which is good for health'}
]

# Iterate over each dictionary in the list word_m
for m in word_m:
    # Iterate over each item (key-value pair) in the current dictionary
    for item in m.items():
        # Print the key-value pair
        print(item)

# Define a new dictionary with a word-description pair
word = {'Elephant': 'Which eats'}

# Append the new dictionary to the list word_m
word_m.append(word)

# Print a message indicating that a new dictionary has been appended to the list
print()
print('Appending the list of dictionary ')
print()

# Iterate over each dictionary in the updated list word_m
for m in word_m:
    # Iterate over each item (key-value pair) in the current dictionary
    for item in m.items():
        # Print the key-value pair
        print(item)

# Print a message indicating that the dictionary will be reversed (values first, then keys)
print()
print('Reversing the dictionary ')
print()

# Iterate over each dictionary in the list word_m
for m in word_m:
    # Iterate over each item (key-value pair) in the current dictionary
    for item, values in m.items():
        # Print the value first, then the key
        print(f'{values}: {item}', end='\n')
