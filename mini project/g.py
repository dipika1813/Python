import random

def roll_dice():


    return random.randint(1, 6)

# Example usage
while True:
    input("Press Enter to roll the dice or type 'q' to quit: ")
    result = roll_dice()
    print(f"You rolled a {result}")
    
    again = input("Roll again.. ").lower()
    print("you rolled a" ,roll_dice())