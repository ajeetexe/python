def binary_to_hexadecimal(num):
    x = num
    res = []
    while num > 0:
        mod = num % 10000
        if mod == 0:
            res.append(0)
        elif mod == 1:
            res.append(1)
        elif mod == 10:
            res.append(2)
        elif mod == 11:
            res.append(3)
        elif mod == 100:
            res.append(4)
        elif mod == 101:
            res.append(5)
        elif mod == 110:
            res.append(6)
        elif mod == 111:
            res.append(7)
        elif mod == 111:
            res.append(7)
        elif mod == 1000:
            res.append(8)
        elif mod == 1001:
            res.append(9)
        elif mod == 1010:
            res.append("A")
        elif mod == 1011:
            res.append("B")
        elif mod == 1100:
            res.append("C")
        elif mod == 1101:
            res.append("D")
        elif mod == 1110:
            res.append("E")
        elif mod == 1111:
            res.append("F")
        else:
            return 'Digit must be between 0 and 1'
            break
        num = num // 10000
    string = ''
    for j in res[::-1]:
        string = string + str(j)
    return f'Hexadecimal Number of ({x})\u2082 is ({string})\u2081\u2086'


num = int(input('Enter Binary'))
print(binary_to_hexadecimal(num))
