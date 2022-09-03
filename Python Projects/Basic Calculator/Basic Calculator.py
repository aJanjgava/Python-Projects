"""
    Building the simple calculator with Python
        Calculator functions:
            1. addition; 2. subtraction; 3.multiplication; 4. division;
"""


def add(num1, num2):
    answer = num1 + num2
    print(str(num1) + '+' + str(num2) + '=' + str(answer))


def sub(num1, num2):
    answer = num1 - num2
    print(str(num1) + '-' + str(num2) + '=' + str(answer))


def mul(num1, num2):
    answer = num1 * num2
    print(str(num1) + '*' + str(num2) + '=' + str(answer))


def div(num1, num2):
    answer = num1 / num2
    print(str(num1) + '/' + str(num2) + '=' + str(answer))


while True:

    print('\nCalculator Operations:')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exit Calculator')

    choice = input('Enter your choice: ')

    if choice == '1':
        print('\nAddition')
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        add(num1, num2)

    elif choice == '2':
        print('\nSubtraction')
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        sub(num1, num2)

    elif choice == '3':
        print('\nMultiplication')
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        mul(num1, num2)

    elif choice == '4':
        print('\nDivision')
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        div(num1, num2)

    elif choice == '5':
        print('\nEnd of the program!')
        quit()
