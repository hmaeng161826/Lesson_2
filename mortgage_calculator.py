def prompt(message):
    print(f'==>{message}')

def invalid_input(input):
    try:
        number = float(input)
        if number <= 0:
            raise ValueError('Value must be > 0')
    except ValueError:
        return True
    return False
        
prompt('Welcome to Mortgage/Car Payment Calculator!')

while True:
    prompt('Please enter the loan amount in dollars.')
    loan_amount = input()
    while invalid_input(loan_amount):
        prompt('Hmm..invalid input. Please enter a valid loan amount')
        loan_amount = input()

    prompt('Please enter the Annual Percentage Rate(APR).')
    apr = input()
    while invalid_input(apr):
        prompt('Hmm..invalid input. Please enter a valid APR (just number)')
        apr = input()

    prompt('Please enter the loan duration in years')
    loan_duration = input()
    while invalid_input(loan_duration):
        prompt('Hmm..invalid input. Please enter a valid loan duration years')
        loan_duration = input()

    monthly_interest_rate = float(apr) / 100 / 12
    loan_duration_months = int(loan_duration) * 12
    monthly_payment = float(loan_amount) * monthly_interest_rate / (
        1 - (1 + monthly_interest_rate) ** (
            -loan_duration_months))
    
    prompt(f'The monthly payment amount is $'
           f'{monthly_payment:.2f}.')
    
    prompt('Would you like to do another calculation? (y/n)')
    response = input().lower()
    while True:
        if response.startswith('y') or response.startswith('n'):
            break
        prompt("Please enter either 'y' or 'n'.")
        response =input().lower()
    if response != 'y':
        break
