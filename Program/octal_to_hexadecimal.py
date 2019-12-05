def octal_to_hexadecimal(num):
    x = num
    a = 0
    decimal = 0
    while num != 0:
        mod = num % 10
        if mod < 8:
            decimal = decimal + mod * 8 ** a
            a = a + 1
        else:
            return 'Digit greater than 8 not allowed'
            break
        num = num // 10
    res = []
    while decimal > 0:
        hexadecimal = decimal % 16
        decimal = decimal // 16
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
    return f'Decimal Number of ({x})\u2088 is ({string})\u2081\u2086'
num = int(input("Enter Octal Number (Digit between 0 to 7)"))
print(octal_to_hexadecimal(num))