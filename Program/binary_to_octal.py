def binary_to_octal(num):
    x = num
    res = []
    while num > 0:
        mod = num % 1000
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
        else:
            return 'Digit must be between 0 and 1'
            break
        num = num // 1000
    string = ''
    for j in res[::-1]:
        string = string + str(j)
    return f'Octal Number of ({x})\u2082 is ({string})\u2088'

num = int(input('Enter Binary'))
print(binary_to_octal(num))