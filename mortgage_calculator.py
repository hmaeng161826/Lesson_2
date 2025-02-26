def prompt(message):
    print(f'==>{message}')

prompt('Welcome to Mortgage/Car Payment Calculator!')

while True:
    while True:
        prompt('Please enter the loan amount in dollars.')
        loan_amount = input()
        if float(loan_amount):
            break
        prompt('Hmm..invalid input. Please enter a valid loan amount')
    while True:
        prompt('Please enter the Annual Percentage Rate(APR).')
        apr = input()
        if float(apr):
            break
        prompt('Hmm..invalid input. Please enter a valid APR (just number)')
    while True:
        prompt('Please enter the loan duration in years')
        loan_duration = input()
        if float(loan_duration):
            break
        prompt('Hmm..invalid input. Please enter a valid loan duration years')
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
