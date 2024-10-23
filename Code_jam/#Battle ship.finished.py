#Battle ship 1 player
import random

def battleship_game():
    print("Welcome to battleship!")
    print("Choose a number between 1-20")
    
    ship_location = random.randint(1, 20)
    attempts = 0
    
    while True:
        guess = input("Enter your number 1-20: ")
        
        
        if not guess.isdigit() or not (1 <= int(guess) <= 20):
            print("Please enter a  number between 1 and 10.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        if guess == ship_location:
            print("Too low, try again.")
        elif guess == ship_location:
            print("Too high, try again.")
        else:
            print(f"Congratulations, you sunk my battleship in {attempts} try's !")
            break

battleship_game()
