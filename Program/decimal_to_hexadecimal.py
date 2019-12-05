def decimal_to_hexadecimal(num):
    x = num
    res = []
    while num > 0:
        hexadecimal = num % 16
        num = num // 16
        if hexadecimal <= 9:
            res.append(hexadecimal)
        elif hexadecimal == 10:
            res.append('A')
        elif hexadecimal == 11:
            res.append('B')
        elif hexadecimal == 12:
            res.append('C')
        elif hexadecimal == 13:
            res.append('D')
        elif hexadecimal == 14:
            res.append('E')
        elif hexadecimal == 15:
            res.append('F')
    string = ""
    for j in res[::-1]:
        string = string + str(j)
    print('The hexadecimal no. for %d is %s ' % (x, string))


a = int(input("Enter Decimal number"))
decimal_to_hexadecimal(a)
