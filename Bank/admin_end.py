from tkinter import *
from backend import *
from tkinter import ttk
from create_account import CreateAccount

database = Database('bank.db')


class Admin(object):

    def __init__(self, admin):
        self.admin = admin
        self.admin.wm_title('Ajeet Bank    --For Admin')
        self.admin.resizable(0, 0)
        f = Frame(admin, bg='#fff', width=500, height=300)
        f.grid(row=0, column=0, sticky="NW")
        f.grid_propagate(0)
        f.update()
        label_upd = Label(admin, text='Enter here to to perform action', bg='white')
        label_upd.place(x=10, y=10)
        entry_upd = StringVar()
        self.entry_update = ttk.Entry(admin, textvariable=entry_upd)
        self.entry_update.place(x=200, y=10)
        self.combo_update = ttk.Combobox(admin, state="readonly", values=[
            "Select Here to Update",
            "Name",
            "Balance",
            "Address"
        ])
        self.combo_update.place(x=350, y=10)
        self.combo_update.current(0)
        self.list_view = Listbox(admin, height=13, width=35, fg='red', font=('Courier New', 10))
        self.list_view.place(x=10, y=50)
        sb = Scrollbar(admin)
        self.list_view.config(yscrollcommand=sb.set)
        sb.configure(command=self.list_view.yview)
        self.list_view.bind('<<ListboxSelect>>', self.get_selected_row)
        sb.place(x=295, y=50)
        button_create = Button(admin, text='Create Account', font=('Courier New', 11), command=self.create_command)
        button_create.place(x=350, y=50)
        button_view = Button(admin, text='View Account', font=('Courier New', 11), command=self.view_command)
        button_view.place(x=350, y=100)
        button_search = Button(admin, text='Search Account', font=('Courier New', 11), command=self.search_command)
        button_search.place(x=350, y=150)
        button_update = Button(admin, text='Update Account', font=('Courier New', 11), command=self.update_command)
        button_update.place(x=350, y=200)
        button_delete = Button(admin, text='Delete Account', font=('Courier New', 11), command=self.delete_command)
        button_delete.place(x=350, y=250)

    def get_selected_row(self, event):
        try:
            index = self.list_view.curselection()[0]
            self.selected = self.list_view.get(index)
        except IndexError:
            pass

    def create_command(self):
        create = Tk()
        CreateAccount(create)

    def view_command(self):
        self.list_view.delete(0, END)
        for row in database.view():
            self.list_view.insert(END, row)

    def search_command(self):
        self.list_view.delete(0, END)
        for row in database.search(self.entry_update.get(), self.entry_update.get(), self.entry_update.get(),
                                   self.entry_update.get()):
            self.list_view.insert(END, row)

    def update_command(self):
        if self.combo_update.current() == 1:
            database.update(self.selected[0], self.entry_update.get(), self.selected[2], self.selected[3],
                            self.selected[4])
            self.view_command()
        elif self.combo_update.current() == 2:
            database.update(self.selected[0], self.selected[1], self.entry_update.get(), self.selected[3],
                            self.selected[4])
            self.view_command()
        elif self.combo_update.current() == 3:
            database.update(self.selected[0], self.selected[1], self.selected[2],
                            self.selected[3], self.entry_update.get(), )
            self.view_command()

    def delete_command(self):
        database.delete(self.selected[0])
        self.view_command()
