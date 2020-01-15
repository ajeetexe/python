from tkinter import Tk, Button, Label, Frame, Entry, IntVar, END


class Calc:
    def __init__(self, master):
        master.title("Caculator")
        master.minsize(400, 500)
        master.resizable(0, 0)
        master.config(bg="Indigo")
    
        value = IntVar()
        self.resBox = Entry(master, textvariable=value,font=('Helvetica','20'),justify='right')
        self.resBox.place(x=50,y=50,width=300,height=50)

        cancelBtn = Button(master, text="C",font=('Helvetica','20'),command=self.can)
        cancelBtn.place(x=50, y=132,width=75,height=66)

        deleteBtn = Button(master, text="➤",font=('Helvetica','20'),command=self.dele)
        deleteBtn.place(x=125, y=132,width=75,height=66)

        percentageBtn = Button(master, text="%",font=('Helvetica','20'),command=self.per)
        percentageBtn.place(x=200, y=132,width=75,height=66)

        divideBtn = Button(master, text="➗",font=('Helvetica','20'),command=self.div)
        divideBtn.place(x=275, y=132,width=75,height=66)

        sevenBtn = Button(master, text="7",font=('Helvetica','20'),command=self.seven)
        sevenBtn.place(x=50, y=198,width=75,height=66)

        eightlBtn = Button(master, text="8",font=('Helvetica','20'),command=self.eight)
        eightlBtn.place(x=125, y=198,width=75,height=66)

        nineBtn = Button(master, text="9",font=('Helvetica','20'),command=self.nine)
        nineBtn.place(x=200, y=198,width=75,height=66)

        multiplyBtn = Button(master, text="x",font=('Helvetica','20'),command=self.mul)
        multiplyBtn.place(x=275, y=198,width=75,height=66)

        fourBtn = Button(master, text="4",font=('Helvetica','20'),command=self.four)
        fourBtn.place(x=50, y=264,width=75,height=66)

        fiveBtn = Button(master, text="5",font=('Helvetica','20'),command=self.five)
        fiveBtn.place(x=125, y=264,width=75,height=66)

        sixBtn = Button(master, text="6",font=('Helvetica','20'),command=self.six)
        sixBtn.place(x=200, y=264,width=75,height=66)

        minusBtn = Button(master, text="-",font=('Helvetica','20'),command=self.minus)
        minusBtn.place(x=275, y=264,width=75,height=66)

        oneBtn = Button(master, text="1",font=('Helvetica','20'),command=self.one)
        oneBtn.place(x=50, y=330,width=75,height=66)

        twoBtn = Button(master, text="2",font=('Helvetica','20'),command=self.two)
        twoBtn.place(x=125, y=330,width=75,height=66)

        threeBtn = Button(master, text="3",font=('Helvetica','20'),command=self.three)
        threeBtn.place(x=200, y=330,width=75,height=66)

        plusBtn = Button(master, text="+",font=('Helvetica','20'),command=self.plus)
        plusBtn.place(x=275, y=330,width=75,height=66)

        zeroBtn = Button(master, text="0",font=('Helvetica','20'),command=self.zero)
        zeroBtn.place(x=50, y=396,width=75,height=66)

        dotBtn = Button(master, text=".",font=('Helvetica','20'),command=self.dot)
        dotBtn.place(x=125, y=396,width=75,height=66)

        equalBtn = Button(master, text="=",font=('Helvetica','20'),command=self.equal)
        equalBtn.place(x=200, y=396,width=150,height=66)


    def zero(self):
        self.resBox.insert(END,0)

    def one(self):
        self.resBox.insert(END,1)
    
    def two(self):
        self.resBox.insert(END,2)

    def three(self):
        self.resBox.insert(END,3)

    def four(self):
        self.resBox.insert(END,3)

    def five(self):
        self.resBox.insert(END,3)

    def six(self):
        self.resBox.insert(END,3)

    def seven(self):
        self.resBox.insert(END,3)

    def eight(self):
        self.resBox.insert(END,3)

    def nine(self):
        self.resBox.insert(END,3)

    def dot(self):
        self.resBox.insert(END,3)

    def plus(self):
        self.resBox.insert(END,3)

    def minus(self):
        self.resBox.insert(END,3)

    def mul(self):
        self.resBox.insert(END,3)

    def div(self):
        self.resBox.insert(END,3)

    def per(self):
        self.resBox.insert(END,3)

    def can(self):
        self.resBox.insert(END,3)

    def dele(self):
        self.resBox.insert(END,3)

    def equal(self):
        pass

if __name__ == "__main__":
    root = Tk()
    Calc(root)
    root.mainloop()
