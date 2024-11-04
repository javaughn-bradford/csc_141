#09_13_dice

import random

class Die:
    def __init__(self, sides=6):
        """Initialize the die with a specific side"""
        self.sides = sides

    def roll_die(self):
        """Roll the die and from a random number between 1 and 6"""
        return random.randint(1, self.sides)

# Function to roll the die multiple times
def roll_dice(die, rolls=10):
    """Roll the given die 10 times and print the results."""
    results = [die.roll_die() for _ in range(rolls)]
    print(f"The numbers rolled of the {die.sides}-sided die {rolls} times: {results}")


six_sided_die = Die()
ten_sided_die = Die(10)
twenty_sided_die = Die(20)

roll_dice(six_sided_die)
roll_dice(ten_sided_die)
roll_dice(twenty_sided_die)
