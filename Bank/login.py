from tkinter import *
from tkinter import messagebox

from admin_end import Admin
from backend import Database
from user_end import User

database = Database('bank.db')


def main():
    login = Tk()
    Login(login)
    login.mainloop()


class Login:
    def __init__(self, login):
        self.login = login
        self.login.wm_title('Ajeet Bank')
        self.login.resizable(0, 0)
        f = Frame(login, bg='#fff', width=500, height=300)
        f.grid(row=0, column=0, sticky="NW")
        f.grid_propagate(0)
        f.update()
        title_label = Label(login, text="Login", bg="#fff")
        title_label.place(x=50, y=0)
        title_label.config(font=("Blackoak Std", 40))
        l1 = Label(login, text='Name', bg="#fff")
        l1.place(x=50, y=100)
        l1.config(font=("Consolas", 20))
        l2 = Label(login, text="Account No.", bg='#fff')
        l2.place(x=50, y=160)
        l2.config(font=("Consolas", 20))
        name = StringVar()
        self.t1 = Entry(login, textvariable=name, width=35)
        self.t1.place(x=230, y=110)
        self.t1.focus()
        self.t1.bind('<Return>', lambda func1: self.t2.focus())
        acc = StringVar()
        self.t2 = Entry(login, textvariable=acc, width=35)
        self.t2.place(x=230, y=170)
        self.t2.bind('<Return>', lambda func1: login_button.focus())
        login_button = Button(login, text='Login', bg='#fff', fg='#FF4500', command=self.login_command)
        login_button.place(x=220, y=250)
        login_button.config(font=('Consolas', 20))
        login_button.bind('<Return>', lambda func1: self.login_command())

    def login_command(self):
        if (self.t1.get(), self.t2.get()) == self.search_login():
            user = Tk()
            User(user, self.t1.get(), self.t2.get())
            self.login.destroy()
        elif self.t1.get() == "admin" and self.t2.get() == "12345":
            admin = Tk()
            Admin(admin)
            self.login.destroy()
        elif self.t1.get() == "" and self.t2.get() == "":
            messagebox.showwarning("Warning", "You didn't Entered anything, Please Enter Your Account Number and"
                                              " Your Name")
        elif self.t1.get() == "":
            messagebox.showwarning("Warning", "You didn't Entered Name, Please Enter Your Name ")
        elif self.t2.get() == "":
            messagebox.showwarning("Warning",
                                   "You didn't Entered Account Number, Please Enter Your your Account Number")
        else:
            messagebox.showerror('Error', " Name and Account Number didn't match")

    def search_login(self):
        for row in database.search(name=self.t1.get(), account_no=self.t2.get()):
            return row[1], str(row[3])


if __name__ == '__main__':
    main()
