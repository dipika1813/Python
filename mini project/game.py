import random 

choices =["rock", "paper", "scissor"]

def decide_winner(player, computer):
    if(player == computer):
        return "its a tie"
    elif(player == "rock" and computer== "scissor")or\
        (player == "paper" and computer =="rock") or\
        (player == "scissor" and computer=="paper"):
        return "you win!"
        
    else:
        return "computer wins"

while True:
    print("\n --rock, paper, scissor")
    player_choice= input("enter your choice(rock/paper/scissor or 'q'to quit):").lower()

    if (player_choice=="q"):
        print("thanks for playing..")
        break

    if player_choice not in choices:
        print("invalid choice! try again")
        continue
    
    computer_choice= random.choice(choices)
    print(f"you chose : {player_choice}")
    print(f"computer chose : {computer_choice}")

    result= decide_winner(player_choice,computer_choice)
    print(result)