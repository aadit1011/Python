# Importing the numpy library for numerical operations
import numpy as np;

# Taking input from the user for the total number of coin tosses
toss = int(input('Enter the total number of toss='));

# Simulating the coin tosses using np.random.randint which generates random integers (0 or 1)
# 0 represents heads and 1 represents tails
result = np.random.randint(0, 2, toss);

# Counting the number of heads (0s) in the result array
head = np.sum(result == 0);

# Counting the number of tails (1s) in the result array
tail = np.sum(result == 1);

# Calculating the probability of getting heads
probability_of_head = head / toss;

# Calculating the probability of getting tails
probability_of_tail = tail / toss;

# Printing the results including the number of heads, number of tails, and their respective probabilities
print(f'In your total {toss} tosses\nThere were {head} heads\nThere were {tail} tails.\nHence the probability of head is = {probability_of_head}\nThe probability of tail is = {probability_of_tail}');
