def prompt(message):
    print(f'=>{message}')

def invalid(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    
    return False

prompt('Welcome to calculator!')

prompt('Enter the first number: ')
num1 = input()
while invalid(num1):
    prompt("Hmm... that doesn't look like a valid number")
    num1 = input()

prompt('Enter the second number: ')
num2 = input()
while invalid(num2):
    prompt("Hmm... that doesn't look like a valid number")
    num2 = input()

prompt("Enter the type of operation to perform: 'add', 'subtract',"
                  "'multiply' or 'divide': ")
operation = input()
while operation not in ['add', 'subtract', 'multiply', 'divide']:
    prompt("Hmm... that doesn't look like a valid number")
    operation = input()

match operation:
    case 'add':
        output = int(num1) + int(num2)
    case 'subtract':
        output = int(num1)- int(num2)
    case 'multiply':
        output = int(num1) * int(num2)
    case 'divide':
        output = int(num1)/ int(num2)
        
print(f'The result is {output}')
