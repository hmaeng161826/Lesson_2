import json
with open('calculator_messages.json', 'r') as file:
    MESSAEGS = json.load(file)
#ask the user to select a language. the selection should be indexed from the 
#json key.

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    
    except ValueError:
        return True

    return False

def calculator():
    prompt(MESSAEGS['greeting'][language])
    prompt(MESSAEGS['first_number'][language])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAEGS['invalid_number'][language])
        number1 = input()

    prompt(MESSAEGS['second_number'][language])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAEGS['invalid_number'][language])
        number2 = input()

    prompt(MESSAEGS['operation'][language])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(MESSAEGS['invalid_operation'][language])
        operation = input()
    
    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    prompt(f"The result is {output}")

prompt("Please choose a language(언어를 선택해주세요): 'en'(영어) or 'kr'(한국어): ")
language = input()
while language != 'en' and language != 'kr':
    prompt("Wrong input..choose between 'en' or 'kr. 'en' 또는 'kr' 중에서 선택")
    language = input()

while True:
    calculator()
    prompt(MESSAEGS['another_calculation'][language])
    response = input().lower()
    if response and response[0] != 'y':
        break
    
