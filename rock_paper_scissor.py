# pylint: disable=invalid-name

import random
GAME_NAME = 'rock, paper, scissors, lizard, spock'

TOTAL_ROUNDS = 5

WINNING_SCORES = 3

GAME_RULE = (
    f'You will be playing {GAME_NAME} against the computer. '
    f'There will be a total of {TOTAL_ROUNDS} unless you quit before it. '
    f'Whoever wins {WINNING_SCORES} rounds first will be the grand winner!'
    )

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

CHOICE_SHORTCUTS = {
    'r' : 'rock',
    'p' : 'paper',
    'sc' : 'scissors',
    'l' : 'lizard',
    'sp' : 'spock',
}

VALID_KEYS = list(CHOICE_SHORTCUTS.keys())

WINNING_COMBOS = {
    'rock': ['scissors', 'lizard'],
    'scissors': ['paper', 'lizard'],
    'paper': ['rock', 'spock'],
    'lizard': ['paper', 'spock'],
    'spock': ['scissors', 'rock'],
}


score = {
    'player' : 0,
    'computer' : 0,
}

def prompt(message):
    print(f'==>{message}')

def display_initial_msg():
    prompt(f'Welcome to {GAME_NAME}!')
    prompt(GAME_RULE)

def invalid(player_option, valid_option_1, valid_option_2):
    return player_option not in valid_option_1 + valid_option_2

def ask_choice(game_round):
    prompt(f'Round {game_round}!')
    prompt(f"Choose one: {', '.join(VALID_CHOICES)}"
           f"(or shortcuts: r, p, sc, l, sp)")
    player_choice = input().lower()

    while invalid(player_choice, VALID_CHOICES, VALID_KEYS):
        prompt(f"Please enter a valid input: {', '.join(VALID_CHOICES)}"
               f"(or {', '.join(VALID_KEYS)})")
        player_choice = input().lower()

    if player_choice in VALID_KEYS:
        player_choice = CHOICE_SHORTCUTS[player_choice]

    computer_choice = random.choice(VALID_CHOICES)

    return player_choice, computer_choice

def display_winner(player_choice, computer_choice):
    prompt(f'You chose {player_choice}!')
    prompt(f'The computer chose {computer_choice}!')

    if computer_choice in WINNING_COMBOS[player_choice]:
        score['player'] += 1
        prompt('You win!')
    elif computer_choice == player_choice:
        prompt("It's a tie!")
    else:
        score['computer'] += 1
        prompt('Computer wins!')

def display_current_score():
    prompt(f'The Current Score -> Computer {score['computer']} : '
           f'You {score['player']}')

def grand_winner():
    if score['computer'] == WINNING_SCORES:
        return 'computer'

    if score['player'] == WINNING_SCORES:
        return 'you'

def ask_play_again():
    prompt('Do you want to play again (y/n)?')
    response = input().lower()

    while True:
        if response[0] == 'y':
            return True
        elif response[0] == 'n':
            return False
        else:
            prompt("Invalid input. Please enter 'y' or 'n'.")
            response = input().lower()

def play_game():
    game_round = 1
    while game_round <= TOTAL_ROUNDS:
        display_initial_msg()

        player_choice, computer_choice = ask_choice(game_round)

        display_winner(player_choice, computer_choice)

        display_current_score()

        if grand_winner():
            prompt(f'The grand winnder is {grand_winner()}!')
            break

        game_round += 1

        if not ask_play_again():
            prompt('Thank you for playing. Goodbye!')
            break


play_game()
