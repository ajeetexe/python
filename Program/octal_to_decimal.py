def octal_to_decimal(num):
    x = num
    a = 0
    decimal = 0
    while num != 0:
        mod = num % 10
        if mod < 8:
            decimal = decimal + mod * 8 ** a
            a = a + 1
        else:
            return 'Digit greater than 8 not allowed'
            break
        num = num // 10
    return f'Decimal Number of ({x})\u2088 is ({decimal})\u2081\u2080'

num = int(input('Enter Octal Number: '))
print(octal_to_decimal(num))

"""
Subscript and Superscript unicode:-
 \ u208x this for subscript in number it support only 0 to 9
 \ u209x this for subscript in alphabet
 \ u00Bx this superscript   
"""