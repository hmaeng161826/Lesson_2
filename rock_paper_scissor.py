import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
CHOICE_SHORTCUTS = {
    'r' : 'rock',
    'p' : 'paper',
    'sc' : 'scissors',
    'l' : 'lizard',
    's' : 'spock',
}
SHORTCUTS_KEYS = list(CHOICE_SHORTCUTS.keys())

def prompt(message):
    print(f'==>{message}')

def invalid(input, valid_choices):
    return input not in valid_choices

prompt('Welcome to Rock Paper Scissors Spock Lizard')

while True:
    prompt(f"Choose one: {', '.join(VALID_CHOICES)} or shortcuts: r, p, sc, l, s ")
    user_choice = input().lower()
    while user_choice not in VALID_CHOICES and user_choice not in SHORTCUTS_KEYS:
        prompt(f"Please enter a valid input: {', '.join(VALID_CHOICES)} or {', '.join(SHORTCUTS_KEYS)}")
        user_choice = input().lower()
    if user_choice in SHORTCUTS_KEYS:
        user_choice = CHOICE_SHORTCUTS[user_choice]

    computer_choice = random.choice(VALID_CHOICES)
    prompt(f'You chose {user_choice}!')
    prompt(f'The computer chose {computer_choice}!')

    if (
    ((user_choice == 'rock' or user_choice == 'spock') and computer_choice == 'paper') or
    ((user_choice == 'paper' or user_choice =='lizard') and computer_choice == 'scissors') or
    ((user_choice == 'scissors' or user_choice == 'lizard') and computer_choice == 'rock') or
    ((user_choice == 'paper' or user_choice == 'spock') and computer_choice == 'lizard') or
    ((user_choice == 'scissors' or user_choice == 'rock') and computer_choice == 'spock')
    ):
        prompt("Computer wins!")
    elif (
    (user_choice == 'rock' and (computer_choice == 'scissors' or computer_choice == 'lizard')) or
    (user_choice == 'scissors' and (computer_choice == 'paper' or computer_choice == 'lizard')) or
    (user_choice == 'paper' and (computer_choice == 'rock' or computer_choice == 'spock')) or
    (user_choice == 'lizard' and (computer_choice == 'paper' or computer_choice == 'spock')) or
    (user_choice == 'spock' and (computer_choice == 'scissors' or computer_choice == 'rock'))
    ):
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


