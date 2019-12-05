def isprime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


n = int(input('Enter Number'))
if isprime(n):
    print("This is prime Number ")
else:
    print("This is not a prime number")