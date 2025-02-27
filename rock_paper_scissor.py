import random
import pdb

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'==>{message}')

def invalid(string, choices):
    return string not in choices

prompt('Welcome to Rock Paper Scissors')

while True:
    prompt(f"Choose one: {', '.join(VALID_CHOICES)} ")
    user_choice = input()

    while invalid(user_choice, VALID_CHOICES):
        prompt("Please enter a valid input: 'rock', 'paper', or 'scissors")
        user_choice = input()

    computer_choice = random.choice(VALID_CHOICES)
    prompt(f'The computer chose {computer_choice}!')

    if ((user_choice == 'rock' and computer_choice == 'paper') or
    (user_choice == 'paper' and computer_choice == 'scissors') or
    (user_choice == 'scissors' and computer_choice == 'rock')):
        prompt("Computer wins!")
    elif ((user_choice == 'rock' and computer_choice == 'scissors') or
    (user_choice == 'scissors' and computer_choice == 'paper') or
    (user_choice == 'paper' and computer_choice == 'rock')):
        prompt("You win!")
    else:
        prompt("It's a tie!")

    prompt('Do you want to play again (y/n)?') 
    response = input().lower()
    while True:
        if response[0] == 'y' or response[0] == 'n':
            break
        prompt("Invalid input. Please enter 'y' or 'n'.")
        response = input().lower()
    if response[0] != 'y':
        break       


