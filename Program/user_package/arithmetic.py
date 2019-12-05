def add(a, b):
    try:
        c = a + b
        return c
    except ValueError:
        print('Invalid entry, Enter only number.')


def subtract(a, b):
    try:
        c = a - b
        return c
    except ValueError:
        print('Invalid entry, Enter only number.')


def multiply(a, b):
    try:
        c = a * b
        return c
    except ValueError:
        return 'Invalid entry, Enter only number.'


def divide(a, b):
    try:
        c = a / b
        return c
    except ValueError:
        return 'Invalid entry, Enter only number.'
    except ZeroDivisionError:
        return 'Cant divide by Zero'
