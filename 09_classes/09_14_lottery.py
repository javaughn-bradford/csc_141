#09_14_lottery 

import random

# a list of 10 numbers and 5 letters
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# picking four of them from the list
winning_combination = random.sample(items, 4)

# the winning lottery
print(f"Congratulations! Any ticket matching these four items wins a prize: {winning_combination}")
