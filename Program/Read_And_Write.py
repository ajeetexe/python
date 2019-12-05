with open("document/demo.txt", "a+") as file:
    msg = input("Enter Something ")
    file.write(msg)
    file.seek(0)  # seek is used to move the cursor.
    # file = open("demo.txt", "r") , this statement is not used if we use a+ mod.
    print(file.read())
