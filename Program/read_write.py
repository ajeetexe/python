with open('document/demo.txt', 'a+') as file:
    msg = input('Enter message')
    file.write(msg)
    file.seek(0)
    content = file.read()
    print(content)
