def binary_to_decimal(num):
    dec1 = 0
    x = num
    i = 0
    while num != 0:
        rem = num % 10
        if rem == 1 or rem == 0:
            dec = rem * 2 ** i
            dec1 = dec1 + dec
            num = num // 10
            i = i + 1
        else:
            print('Number is not Binary')
            break
    print(f'Decimal Number of {x} is {dec1}')


num1 = int(input('Enter Binary Number'))
binary_to_decimal(num1)
