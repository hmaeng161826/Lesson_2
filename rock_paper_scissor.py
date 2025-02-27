import random

def prompt(message):
    print(f'==>{message}')

def invalid(string):
    global choices
    if string in choices:
        return False
    return True

prompt('Welcome to Rock Paper Scissors')

while True:
    choices = ['rock', 'paper', 'scissors']
    prompt("Enter 'rock', 'paper', or 'scissors: ")
    user_choice = input()

    while invalid(user_choice):
        prompt("Please enter a valid input: 'rock', 'paper', or 'scissors")
        user_choice = input()

    computer_choice = random.choice(choices)
    prompt(f'The computer chose {computer_choice}!')

    if user_choice == 'rock':
        match computer_choice:
            case 'rock':
                prompt("It's a tie!")
            case 'paper':
                prompt('Computer wins!')            
            case 'scissors':
                prompt('You win!')
    elif user_choice == 'paper':
        match computer_choice:
            case 'rock':
                prompt("You win!")
            case 'paper':
                prompt("It's a tie!")            
            case 'scissors':
                prompt('Computer wins!')
    elif user_choice == 'scissors':
        match computer_choice:
            case 'rock':
                prompt("Computer wins!")
            case 'paper':
                prompt("You win!")            
            case 'scissors':
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


