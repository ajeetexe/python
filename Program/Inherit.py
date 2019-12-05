class Student:
    @staticmethod
    def student():
        print("Hi I am form Student")


class Teacher(Student):
    @staticmethod
    def teacher():
        print("Hi form Teacher")


Teacher.student()
Teacher.teacher()
