def factorial(args):
    fact = 1
    while args != 0:
        fact = fact * args
        args = args - 1
    return fact


try:
    value = int(input('Enter Number'))
    print(factorial(value))
except ValueError:
    print("Enter Only Integer Number, Please avoid to enter float and String")
