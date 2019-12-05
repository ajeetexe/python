from tkinter import Label, StringVar, Entry, Button, messagebox

from backend import Database

database = Database("bank.db")


class CreateAccount:
    def __init__(self, create_account):
        self.create_account = create_account
        self.create_account.wm_title('Ajeet Bank')
        self.create_account.resizable(0, 0)
        name_lbl = Label(create_account, text="Name")
        name_lbl.grid(row=0, column=0)
        bal_lbl = Label(create_account, text="Balance")
        bal_lbl.grid(row=0, column=2)
        account_lbl = Label(create_account, text='Account No.')
        account_lbl.grid(row=1, column=0)
        address_lbl = Label(create_account, text="Address")
        address_lbl.grid(row=1, column=2)
        name_value = StringVar()
        self.name_entry = Entry(create_account, textvariable=name_value)
        self.name_entry.grid(row=0, column=1)
        self.name_entry.focus()
        self.name_entry.bind('<Return>', lambda func1: self.balance_entry.focus())
        balance_value = StringVar()
        self.balance_entry = Entry(create_account, textvariable=balance_value)
        self.balance_entry.grid(row=0, column=3)
        self.balance_entry.bind('<Return>', lambda func1: self.account_entry.focus())
        account_value = StringVar()
        self.account_entry = Entry(create_account, textvariable=account_value)
        self.account_entry.grid(row=1, column=1)
        self.account_entry.bind('<Return>', lambda func1: self.address_entry.focus())
        address_value = StringVar()
        self.address_entry = Entry(create_account, textvariable=address_value)
        self.address_entry.grid(row=1, column=3)
        self.address_entry.bind('<Return>', lambda func1: btn.focus())
        btn = Button(create_account, text='Submit', command=self.add_member)
        btn.grid(row=3, column=1, columnspan=2)
        btn.bind('<Return>', lambda func1: self.add_member())

    def add_member(self):
        database.insert(self.name_entry.get(), self.balance_entry.get(), self.account_entry.get(),
                        self.address_entry.get())
        if self.name_entry.get() != "":
            messagebox.showinfo("Success", "Account Create Successfully")
            self.create_account.destroy()
        else:
            messagebox.showwarning("Failed", "Account Not Created")
