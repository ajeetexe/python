# TODO Normal Method
file = open('document/demo.txt')   # mode r is default, don't need to write here.
# use variable to print same sentence many time.
content = file.read()
print(content)
# now i can run this many time.
print(content)
# if I don't use variable then cursor reach at last of sentence and second time it can't run.

# After operation finish it is better to close the file.
file.close()

# TODO Advance method
with open('document/demo.txt') as file:
    content = file.read()
print('________________________________________________')
print(content)
print(content)
# Here we don't close the file, file auto closed in this method.
