import json
with open('calculator_messages.json', 'r') as file:
    MESSAEGS = json.load(file)

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def calculator():
    prompt(MESSAEGS['greeting'])
    prompt(MESSAEGS['first_number'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAEGS['invalid_number'])
        number1 = input()

    prompt(MESSAEGS['second_number'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAEGS['invalid_number'])
        number2 = input()

    prompt(MESSAEGS['operation'])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(MESSAEGS['invalid_operation'])
        operation = input()

    match operation:
        case "1":
            output = int(number1) + int(number2)
        case "2":
            output = int(number1) - int(number2)
        case "3":
            output = int(number1) * int(number2)
        case "4":
            output = int(number1) / int(number2)

    prompt(f"The result is {output}")

while True:
    calculator()
    prompt(MESSAEGS['another_calculation'])
    response = input().lower()
    if response and response[0] != 'y':
        break
    
