try:
    math = int(input('Enter Marks in Mathematics '))
    phy = int(input('Enter marks in Physics '))
    che = int(input('Enter marks in Chemistry '))
    eng = int(input('Enter marks in English '))
    hindi = int(input('Enter marks in Hindi '))

    total_marks = math + phy + che + eng + hindi
    per_marks = total_marks / 5
    if per_marks >= 75:
        print(f'Total marks is {total_marks}, percentage is {per_marks} and pass by distinction marks')
    elif 75 > per_marks >= 60:
        print(f'Total marks is {total_marks}, percentage is {per_marks} and pass by First Division')
    elif 60 > per_marks >= 45:
        print(f'Total marks is {total_marks}, percentage is {per_marks} and pass by Second Division')
    elif 45 > per_marks >= 30:
        print(f'Total marks is {total_marks}, percentage is {per_marks} and pass by Third Division')
    else:
        print(f'Total marks is {total_marks}, percentage is {per_marks} and Failed')
except ValueError:
    print('Enter Only Number')
