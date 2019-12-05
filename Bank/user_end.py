from tkinter import *
from tkinter import messagebox

from backend import *

database = Database('bank.db')


class W_cmd:
    def __init__(self, args, acc, remark):
        args.title("Withdraw Money")
        args.resizable(0, 0)
        self.acc = acc
        self.args = args
        self.remark = remark
        l1 = Label(args, text='Enter Cash Amount', bg='white')
        l1.grid(row=0, column=0)
        depo_v = StringVar()
        self.e1 = Entry(args, textvariable=depo_v)
        self.e1.grid(row=1, column=0)
        b1 = Button(args, text='Done', command=self.w_done)
        b1.grid(row=2, column=0)

    def w_done(self):
        for x in database.view():
            if x[3] == int(self.acc) and self.e1.get() != "":
                database.update(x[0], x[1], x[2] - float(self.e1.get()), x[3], x[4])
                messagebox.showinfo('Success', 'Money Withdraw Successfully')
                self.remark.delete(0, END)
                self.remark.insert(END, 'Name {}'.format(x[1]))
                self.remark.insert(END, 'Account No. {}'.format(x[3]))
                self.remark.insert(END, 'Deducted Money  {}'.format(self.e1.get()))
                self.remark.insert(END, 'Total money Left {}'.format(x[2] - float(self.e1.get())))
                self.args.destroy()
                break
        else:
            messagebox.showwarning("Warning", "Please Fill Money")


class D_cmd:
    def __init__(self, args, acc, remark):
        args.title("Withdraw Money")
        args.resizable(0, 0)
        self.acc = acc
        self.args = args
        self.remark = remark
        self.var = IntVar()
        r1 = Radiobutton(args, text='Self', variable=self.var, value=1, command=self.sel)
        r1.grid(row=0, column=0)
        r2 = Radiobutton(args, text='Other', variable=self.var, value=2, command=self.sel)
        r2.grid(row=0, column=1)
        l1 = Label(args, text='Enter Cash Amount', bg='white')
        l1.grid(row=1, column=0)
        l1 = Label(args, text='Enter Account Number', bg='white')
        l1.grid(row=1, column=1)
        depo_v1 = StringVar()
        self.e1 = Entry(args, textvariable=depo_v1)
        self.e1.grid(row=2, column=0)
        depo_v2 = StringVar()
        self.e2 = Entry(args, textvariable=depo_v2)
        self.e2.grid(row=2, column=1)
        b1 = Button(args, text='Done', command=self.w_done)
        b1.grid(row=3, column=0, columnspan=2)

    def w_done(self):
        global x
        print(self.var.get())
        for x in database.view():
            if self.var.get() == 1:
                if x[3] == int(self.acc) and self.e1.get() != "":
                    database.update(x[0], x[1], x[2] + float(self.e1.get()), x[3], x[4])
                    self.remark.delete(0, END)
                    self.remark.insert(END, 'Name {}'.format(x[1]))
                    self.remark.insert(END, 'Account No. {}'.format(x[3]))
                    self.remark.insert(END, 'Deposit Money  {}'.format(self.e1.get()))
                    self.remark.insert(END, 'Total money Left {}'.format(x[2] + float(self.e1.get())))
                    self.args.destroy()
                    break
            elif self.var.get() == 2:
                if str(x[3]) == self.e2.get() and self.e2.get() != "" and self.e1.get() != "":
                    database.update(x[0], x[1], x[2] + float(self.e1.get()), x[3], x[4])
                    self.remark.delete(0, END)
                    self.remark.insert(END, 'Name {}'.format(x[1]))
                    self.remark.insert(END, 'Account No. {}'.format(x[3]))
                    self.remark.insert(END, 'Deposit Money  {}'.format(self.e1.get()))
                    self.remark.insert(END, 'Total money Left {}'.format(x[2] + float(self.e1.get())))
                    self.args.destroy()
                    break
        else:
            messagebox.showwarning('Warning', 'This Account is not Available, Please Enter correct Account Number')

    def sel(self):
        if self.var.get() == 1:
            self.e2.config(state='disable')
        else:
            self.e2.config(state='normal')


class T_cmd:
    def __init__(self, args, acc, remark):
        args.title("Withdraw Money")
        args.resizable(0, 0)
        self.args = args
        self.remark = remark
        self.acc = acc
        l1 = Label(args, text='Enter Cash Amount', bg='white')
        l1.grid(row=0, column=0)
        l2 = Label(args, text='Enter Account Number', bg='white')
        l2.grid(row=0, column=1)
        depo_v1 = StringVar()
        self.e1 = Entry(args, textvariable=depo_v1)
        self.e1.grid(row=1, column=0)
        depo_v = StringVar()
        self.e2 = Entry(args, textvariable=depo_v)
        self.e2.grid(row=1, column=1)
        b1 = Button(args, text='Done', command=self.w_done)
        b1.grid(row=2, column=0, columnspan=2)

    def w_done(self):

        try:
            charge = float(self.e1.get()) * 10 / 100
            transfer = float(self.e1.get()) - charge
            for x in database.view():
                if str(x[3]) == self.e2.get() and self.e2.get() != "" and self.e1.get() != "":
                    database.update(x[0], x[1], x[2] + transfer, x[3], x[4])
                    self.remark.delete(0, END)
                    self.remark.insert(END, '..........Money Transfer To.......')
                    self.remark.insert(END, 'Name {}'.format(x[1]))
                    self.remark.insert(END, 'Account No. {}'.format(x[3]))
                    self.remark.insert(END, 'Transfer money  {}'.format(self.e1.get()))
                    self.remark.insert(END, 'Charge  {}'.format(charge))
                    self.remark.insert(END, 'After Charge   {}'.format(transfer))
                    self.remark.insert(END, "Balance Left {}".format(x[2] + transfer))
                    break
            else:
                messagebox.showwarning('Warning', "Account Not Found, or May be something Error in our side")
            for x1 in database.view():
                if x1[3] == int(self.acc) and self.e1.get() != "" and self.e2.get():
                    database.update(x1[0], x1[1], x1[2] - transfer, x1[3], x1[4])
                    self.remark.insert(END, '')
                    self.remark.insert(END, '..........Money Transfer From.......')
                    self.remark.insert(END, 'Name {}'.format(x1[1]))
                    self.remark.insert(END, 'Account No. {}'.format(x1[3]))
                    self.remark.insert(END, "Balance Left {}".format(x1[2] - transfer))
                    self.args.destroy()
                    break
        except ValueError:
            messagebox.showerror('Error', "May be you didn't Enter anything or incorrect")




class User:
    def __init__(self, user, name, account):
        self.user = user
        self.account = account
        self.user.wm_title('Ajeet Bank')
        self.user.resizable(0, 0)
        f = Frame(user, bg='#fff', width=500, height=300)
        f.grid(row=0, column=0, sticky="NW")
        f.grid_propagate(0)
        f.update()
        lbl_name_label = Label(user, text='Name:', font=("Consolas", 15), bg='white')
        lbl_name_label.place(x=0, y=0)
        lbl_account_label = Label(user, text='Account No.:', font=("Consolas", 15), bg='white')
        lbl_account_label.place(x=250, y=0)
        lbl_name = Label(user, text=name, font=("Consolas", 15), bg='white', fg='green')
        lbl_name.place(x=60, y=0)
        lbl_account = Label(user, text=account, font=("Consolas", 15), bg='white', fg='green')
        lbl_account.place(x=380, y=0)
        withdraw_btn = Button(user, text='Withdraw', font=('Courier New', 11), width=15, command=self.withdraw_command)
        withdraw_btn.place(x=30, y=40)
        deposit_btn = Button(user, text='Deposit', font=('Courier New', 11), width=15, command=self.deposit_command)
        deposit_btn.place(x=180, y=40)
        transfer_btn = Button(user, text='Transfer', font=('Courier New', 11), width=15, command=self.transfer_command)
        transfer_btn.place(x=330, y=40)

        self.remark = Listbox(user, height=12, width=75)
        self.remark.place(x=10, y=80)

    def withdraw_command(self):
        cmd = Tk()
        W_cmd(cmd, self.account, self.remark)

    def deposit_command(self):
        cmd = Tk()
        D_cmd(cmd, self.account, self.remark)

    def transfer_command(self):
        cmd = Tk()
        T_cmd(cmd, self.account, self.remark)
