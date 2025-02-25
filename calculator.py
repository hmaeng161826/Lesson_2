import json

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    
    except ValueError:
        return True

    return False

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

prompt("Please choose a language(언어를 선택해주세요): 'en'(영어) or 'kr'(한국어): ")
language = input()
while language != 'en' and language != 'kr':
    prompt("Wrong input..choose between 'en' or 'kr. 'en' 또는 'kr' 중에서 선택")
    language = input()

prompt(MESSAGES['greeting'][language])
while True:
    while True:
        prompt(MESSAGES['first_number'][language])
        number1 = input()

        if not invalid_number(number1):
            break

        prompt(MESSAGES['invalid_number'][language])
    
    while True:
        prompt(MESSAGES['second_number'][language])
        number2 = input()

        if not invalid_number(number2):
            break

        prompt(MESSAGES['invalid_number'][language])

    while True:
        prompt(MESSAGES['operation'][language])
        operation = input()

        if operation in ["1", "2", "3", "4"]:
            break

        prompt(MESSAGES['invalid_operation'][language])
        
    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    prompt(MESSAGES['result'][language].format(output=output))

    prompt(MESSAGES['another_calculation'][language])
    response = input()
    if response[0].lower() != 'y':
        break
    
