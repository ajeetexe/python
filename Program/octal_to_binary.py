def octal_to_binary(num):
    x = num
    res = []
    while num > 0:            
        binary = num % 10
        if binary == 0:
            res.append("000")
        elif binary == 1:
            res.append("001")
        elif binary == 2:
            res.append("010")
        elif binary == 3:
            res.append("011")
        elif binary == 4:
            res.append("100")
        elif binary == 5:
            res.append("101")
        elif binary == 6:
            res.append("110")
        elif binary == 7:
            res.append("111")
        elif 8 <= binary <= 9:
            return "Please enter a octal number digit between 0 to 7"
            break
        num = num // 10

    string = ""
    for j in res[::-1]:
        string = string + str(j)
    return 'The binary no. for %d is %s ' % (x, string)


a = int(input("Enter Octal number"))
print(octal_to_binary(a))
