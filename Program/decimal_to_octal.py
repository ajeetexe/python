def decimal_to_octal(num):
    x = num
    res = []
    while num > 0:
        octal = num % 8
        res.append(octal)
        num = num // 8

    string = ""
    for j in res[::-1]:
        string = string + str(j)
    print('The octal no. for %d is %s ' % (x, string))


a = int(input("Enter Decimal number"))
decimal_to_octal(a)
