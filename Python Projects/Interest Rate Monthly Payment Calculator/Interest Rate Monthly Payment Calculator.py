"""
    Interest Rate Monthly Payment Calculator
        Necessary data: Principal, apr(Annual interest rate), years
"""


def interest_rate():
    print('This is a monthly payment loan calculator\n')

    principal = float(input('Input the loan amount: '))
    apr = float(input('Input the annual interest rate: '))
    years = int(input('Input amount of years: '))

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))

    print(f'The monthly payment for this loan is: {round(monthly_payment, 2)}')


interest_rate()