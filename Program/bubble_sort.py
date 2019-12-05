def bubble_sort(num):
    n = len(num)
    for i in range(n):
        for j in range(n-1-i):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp


try:
    print("Enter number and number sorted automatically")
    num1 = []
    while True:
        value = input()
        if value == 'q' or value == 'Q':
            break
        elif 'a' <= value <= 'z' or 'A' <= value <= 'Z':
            print("Please Enter Number, To quit enter q\nSorted Number is --> {}".format(num1))
        else:
            num1.append(int(value))
            bubble_sort(num1)
            print(f'Sorted Number is --> {num1}')

except ValueError:
    print()
        
