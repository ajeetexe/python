import tkinter as tk
from tkinter import *


class karl(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Karlos")
        self.button1 = Button(self, text="Click here", width=25, command=self.new_window)
        self.button1.grid(row=0, column=1, columnspan=2, sticky=W+E+N+S)

    def new_window(self):
        self.newWindow = karl2()


class karl2(Frame):
    def __init__(self):
        new = tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("Karlos More Window")
        new.button = tk.Button(text="Press to close", width=25, command=self.close_window)
        new.button.pack()

    def close_window(self):
        self.destroy()


def main():
    karl().mainloop()


if __name__ == '__main__':
    main()