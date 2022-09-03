"""
    Currency Converter
"""


def curr_convert():
    print('This program converts US dollars to Pounds\n')

    dollar = eval(input('Enter the amount in dollars: '))

    pound = convert_to_pounds(dollar)

    print(f'That is {pound} pounds.')


convert_to_pounds = lambda dollars: dollars * 0.82

curr_convert()
