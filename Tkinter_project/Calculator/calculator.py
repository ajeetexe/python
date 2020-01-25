from tkinter import IntVar, Entry, Button, Tk


class Calc:
    isAddition = False
    isMultiplication = False
    isSubtraction = False
    isDivision = False
    # isPercentage = False

    def __init__(self, master):
        master.title("Calculator")
        master.minsize(400, 500)
        master.resizable(0, 0)
        master.config(bg="Indigo")

        self.value = IntVar()
        self.resBox = Entry(master, textvariable=self.value, font=('Helvetica', '20'), justify='right')
        self.resBox.place(x=50, y=50, width=300, height=50)

        cancel_btn = Button(master, text="C", font=('Helvetica', '20'), command=self.can)
        cancel_btn.place(x=50, y=132, width=112, height=66)

        delete_btn = Button(master, text="➤", font=('Helvetica', '20'), command=self.delete)
        delete_btn.place(x=162, y=132, width=112, height=66)

        """
        The Two Button Above is shared some size of percenatage button
        we are not making any percentage button this time.
        """

        # percentage_btn = Button(master, text="%", font=('Helvetica', '20'), command=self.per)
        # percentage_btn.place(x=200, y=132, width=75, height=66)

        divide_btn = Button(master, text="➗", font=('Helvetica', '20'), command=self.div)
        divide_btn.place(x=275, y=132, width=75, height=66)

        seven_btn = Button(master, text="7", font=('Helvetica', '20'), command=self.seven)
        seven_btn.place(x=50, y=198, width=75, height=66)

        eight_btn = Button(master, text="8", font=('Helvetica', '20'), command=self.eight)
        eight_btn.place(x=125, y=198, width=75, height=66)

        nine_btn = Button(master, text="9", font=('Helvetica', '20'), command=self.nine)
        nine_btn.place(x=200, y=198, width=75, height=66)

        multiply_btn = Button(master, text="x", font=('Helvetica', '20'), command=self.mul)
        multiply_btn.place(x=275, y=198, width=75, height=66)

        four_btn = Button(master, text="4", font=('Helvetica', '20'), command=self.four)
        four_btn.place(x=50, y=264, width=75, height=66)

        five_btn = Button(master, text="5", font=('Helvetica', '20'), command=self.five)
        five_btn.place(x=125, y=264, width=75, height=66)

        six_btn = Button(master, text="6", font=('Helvetica', '20'), command=self.six)
        six_btn.place(x=200, y=264, width=75, height=66)

        minus_btn = Button(master, text="-", font=('Helvetica', '20'), command=self.minus)
        minus_btn.place(x=275, y=264, width=75, height=66)

        one_btn = Button(master, text="1", font=('Helvetica', '20'), command=self.one)
        one_btn.place(x=50, y=330, width=75, height=66)

        two_btn = Button(master, text="2", font=('Helvetica', '20'), command=self.two)
        two_btn.place(x=125, y=330, width=75, height=66)

        three_btn = Button(master, text="3", font=('Helvetica', '20'), command=self.three)
        three_btn.place(x=200, y=330, width=75, height=66)

        plus_btn = Button(master, text="+", font=('Helvetica', '20'), command=self.plus)
        plus_btn.place(x=275, y=330, width=75, height=66)

        zero_btn = Button(master, text="0", font=('Helvetica', '20'), command=self.zero)
        zero_btn.place(x=50, y=396, width=75, height=66)

        dot_btn = Button(master, text=".", font=('Helvetica', '20'), command=self.dot)
        dot_btn.place(x=125, y=396, width=75, height=66)

        equal_btn = Button(master, text="=", font=('Helvetica', '20'), command=self.equal)
        equal_btn.place(x=200, y=396, width=150, height=66)

    def data_fetch(self, num):
        data = self.value.get()
        final_data = int(str(data) + str(num))
        self.value.set(final_data)

    def zero(self):
        self.data_fetch(0)

    def one(self):
        self.data_fetch(1)

    def two(self):
        self.data_fetch(2)

    def three(self):
        self.data_fetch(3)

    def four(self):
        self.data_fetch(4)

    def five(self):
        self.data_fetch(5)

    def six(self):
        self.data_fetch(6)

    def seven(self):
        self.data_fetch(7)

    def eight(self):
        self.data_fetch(8)

    def nine(self):
        self.data_fetch(9)

    def dot(self):
        self.data_fetch(3)

    def plus(self):
        self.add = self.value.get()
        self.value.set(0)
        self.isAddition = True

    def minus(self):
        self.minus = self.value.get()
        self.value.set(0)
        self.isSubtraction = True

    def mul(self):
        self.mul = self.value.get()
        self.value.set(0)
        self.isMultiplication = True

    def div(self):
        self.div = self.value.get()
        self.value.set(0)
        self.isDivision = True

    # def per(self):
    #     self.value.set(0)

    def can(self):
        self.value.set(0)

    def delete(self):
        data = self.value.get()
        length = len(str(data))
        if length > 1:
            final_data =int(str(data)[:length-1])
            self.value.set(final_data) 
        else:
            self.value.set(0)

    def equal(self):
        num = self.value.get()
        if self.isAddition:
            res = num + self.add
            self.value.set(res)
            self.isAddition = False
        elif self.isSubtraction:
            res = num - self.minus
            self.value.set(res)
            self.isSubtraction = False
        elif self.isMultiplication:
            res = num * self.mul
            self.value.set(res)
            self.isMultiplication = False
        elif self.isDivision:
            try:
                res = num / self.div
                self.value.set(res)
                self.isDivision = False
            except ZeroDivisionError:
                self.value.set('Error')


if __name__ == "__main__":
    root = Tk()
    Calc(root)
    root.mainloop()
