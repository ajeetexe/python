def decimal_to_binary(num):
    x = num
    res = []
    while num > 0:
        binary = num % 2
        res.append(binary)
        num = num // 2

    string = ""
    for j in res[::-1]:
        string = string + str(j)
    print('The binary no. for %d is %s ' % (x, string))


a = int(input("Enter Decimal number"))
decimal_to_binary(a)
