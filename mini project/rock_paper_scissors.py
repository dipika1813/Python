import random

# List of possible choices
choices = ["rock", "paper", "scissors"]

# Function to determine the winner
def decide_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Game loop
while True:
    print("\n--- Rock, Paper, Scissors ---")
    player_choice = input("Enter your choice (rock/paper/scissors or 'q' to quit): ").lower()

    if player_choice == 'q':
        print("Thanks for playing!")
        break

    if player_choice not in choices:
        print("Invalid choice! Try again.")
        continue

    # Computer randomly picks a choice
    computer_choice = random.choice(choices)

    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    # Decide the winner
    result = decide_winner(player_choice, computer_choice)
    print(result)
