
import random

you_wins = 0
computer_wins = 0

def winner(your_choice, computer_choice):
    global you_wins, computer_wins

    if your_choice == computer_choice:
        print("Tie!")
    elif (
        (your_choice == 'rock' and computer_choice == 'scissors') or
        (your_choice == 'paper' and computer_choice == 'rock') or
        (your_choice == 'scissors' and computer_choice == 'paper')
    ):
        you_wins += 1
        print("You win!")
    else:
        computer_wins += 1
        print("Computer wins!")

def game_play():
    choices = ['rock', 'paper', 'scissors']
    print("Welcome to Rock, Paper, Scissors!")
    print("Please choose one of the following options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")

    player_choice = int(input("Enter your choice (1-4): ")) - 1

    if player_choice == 3:
        print("You have quit the game.")
        return False

    if player_choice < 0 or player_choice >= 3:
        print("Invalid choice. Please try again.")
        return True

    your_choice = choices[player_choice]
    computer_choice = random.choice(choices)

    print("You chose:", your_choice)
    print("Computer chose:", computer_choice)

    winner(your_choice, computer_choice)
    print("Player wins:", you_wins)
    print("Computer wins:", computer_wins)
    return True

while game_play():
    pass
