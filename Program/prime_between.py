def prime(num1, num2):
    for i in range(num1, num2 + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)


a = int(input("Enter Start Number"))
b = int(input("Enter last number"))
prime(a, b)
