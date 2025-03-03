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

def invalid(user_option, valid_option_1, valid_option_2):
    return user_option not in valid_option_1 + valid_option_2

def player_wins(user_choice, computer_choice):
    if(
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'rock' and computer_choice == 'lizard') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'scissors' and computer_choice == 'lizard') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'paper' and computer_choice == 'spock') or
        (user_choice == 'lizard' and computer_choice == 'paper') or
        (user_choice == 'lizard' and computer_choice =='spock') or
        (user_choice == 'spock' and computer_choice == 'scissors') or
        (user_choice == 'spock' and computer_choice == 'rock')
    ):
        return True
    else:
        return False

def display_winner(user, computer, user_winning, computer_winning):
    prompt(f'You chose {user}!')
    prompt(f'The computer chose {computer}!')

    if player_wins(user, computer):
        user_winning += 1
        prompt("You win!")
    elif user == computer:
        prompt("It's a tie!")
    else:
        computer_winning += 1
        prompt("Computer wins!")

    return user_winning, computer_winning

def display_current_score(user_wins_score, computer_wins_score):
    prompt(f'Computer {computer_wins_score} : You {user_wins_score}')

def grand_winner(user_grand_wins, computer_grand_wins):
    if computer_grand_wins == 3:
        return 'computer'

    if user_grand_wins == 3:
        return 'you'

computer_wins = 0
user_wins = 0
game_round = 1

prompt('Welcome to Rock Paper Scissors Spock Lizard')

while game_round <= 5:
    prompt(f'Round {game_round}!')
    prompt(f"Choose one: {', '.join(VALID_CHOICES)}"
           f"(or shortcuts: r, p, sc, l, sp)")
    user_input = input().lower()

    while invalid(user_input, VALID_CHOICES, VALID_KEYS):
        prompt(f"Please enter a valid input: {', '.join(VALID_CHOICES)}"
               f"(or {', '.join(VALID_KEYS)})")
        user_input = input().lower()

    if user_input in VALID_KEYS:
        user_input = CHOICE_SHORTCUTS[user_input]

    computer_input = random.choice(VALID_CHOICES)

    user_wins, computer_wins = display_winner(user_input,
                                computer_input, user_wins, computer_wins)

    display_current_score(user_wins, computer_wins)

    game_round += 1

    if grand_winner(user_wins, computer_wins):
        prompt(f'The grand winner is'
               f'{grand_winner(user_wins, computer_wins)}!')
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
##FINAL##