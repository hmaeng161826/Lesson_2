# pylint: disable=invalid-name

import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

CHOICE_SHORTCUTS = {
    'r' : 'rock',
    'p' : 'paper',
    'sc' : 'scissors',
    'l' : 'lizard',
    'sp' : 'spock',
}
VALID_KEYS = list(CHOICE_SHORTCUTS.keys())

def prompt(message):
    print(f'==>{message}')

def invalid(user_input, valid_option_1, valid_option_2):
    return user_input not in valid_option_1 + valid_option_2

def display_winner(user, computer):
    global user_wins, computer_wins
    prompt(f'You chose {user}!')
    prompt(f'The computer chose {computer}!')

    if (
    (user_choice in ('rock', 'spock') and computer_choice == 'paper')
    or (user_choice in ('paper', 'lizard') and computer_choice == 'scissors')
    or (user_choice in ('scissors', 'lizard') and computer_choice == 'rock')
    or (user_choice in ('paper', 'spock') and computer_choice == 'lizard')
    or (user_choice in ('scissors', 'rock') and computer_choice == 'spock')
    ):
        computer_wins += 1
        prompt("Computer wins!")
        prompt(f'Computer {computer_wins} : You {user_wins}')

    elif (
    (user_choice == 'rock' and computer_choice in ('scissors', 'lizard'))
    or (user_choice == 'scissors' and computer_choice in ('paper', 'lizard'))
    or (user_choice == 'paper' and computer_choice in ('rock', 'spock'))
    or (user_choice == 'lizard' and computer_choice in ('paper', 'spock'))
    or (user_choice == 'spock' and computer_choice in ('scissors', 'rock'))
):
        user_wins += 1
        prompt("You win!")
        display_current_score()
    else:
        prompt("It's a tie!")
        display_current_score()

def grand_winner():
    if computer_wins == 3:
        return 'computer'

    if user_wins == 3:
        return 'you'

def display_current_score():
    prompt(f'Computer {computer_wins} : You {user_wins}')

computer_wins = 0
user_wins = 0
game_round = 1

prompt('Welcome to Rock Paper Scissors Spock Lizard')

while game_round <= 5:
    prompt(f'Round {game_round}!')
    prompt(f"Choose one: {', '.join(VALID_CHOICES)}"
           f"(or shortcuts: r, p, sc, l, sp)")
    user_choice = input().lower()

    while invalid(user_choice, VALID_CHOICES, VALID_KEYS):
        prompt(f"Please enter a valid input: {', '.join(VALID_CHOICES)}"
               f"(or {', '.join(VALID_KEYS)})")
        user_choice = input().lower()

    if user_choice in VALID_KEYS:
        user_choice = CHOICE_SHORTCUTS[user_choice]

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(user_choice, computer_choice)

    game_round += 1

    if grand_winner():
        prompt(f'The grand winner is {grand_winner()}!')
        break

    if game_round > 5:
        break

    prompt('Do you want to play again (y/n)?')
    response = input().lower()

    while True:
        if response[0] == 'y' or response[0] == 'n':
            break
        prompt("Invalid input. Please enter 'y' or 'n'.")
        response = input().lower()

    if response[0] != 'y':
        break
