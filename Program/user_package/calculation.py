def add_of_two_number(v1, v2):
    print(__name__)
    try:
        return v1 + v2
    except ValueError:
        return 'Number Only'
    except NameError:
        return 'Number Only'


def mul_of_two_number(v1, v2):
    try:
        return v1 * v2
    except ValueError:
        return 'Number Only'
    except NameError:
        return 'Number Only'


def sub_of_two_number(v1, v2):
    try:
        return v1 - v2
    except ValueError:
        return 'Number Only'


def div_of_two_number(v1, v2):
    try:
        return v1 / v2
    except ValueError:
        return 'Number Only'
    except ZeroDivisionError:
        return 'Number Not Divided By Zero'
