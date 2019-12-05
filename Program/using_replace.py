phone_numbers = {
    'Rahul': '+919876545234',
    'Mohit': '+918734562356',
    'Ajeet': '+918676991194',
    'Nani': '+918544307150'
}
for value in phone_numbers.values():
    print(value.replace('+91', '00'))


# replace not working with int, float etc, it works only with string.
