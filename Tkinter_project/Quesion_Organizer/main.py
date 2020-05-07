from tkinter import Frame, Button, Listbox, Label, StringVar, Entry, END, Tk, ANCHOR, font, Text
from backend import Database
import os


class QuestionOrganizer:

    def __init__(self):
        self.app = Tk()
        self.app.wm_title('Question Organizer')
        self.app.resizable(0, 0)
        # TODO: Frame1 is created
        frame1 = Frame(self.app, bg='#fff', width=200, height=800)
        frame1.grid(row=0, column=0, sticky='NN')
        frame1.grid_propagate(0)
        frame1.update()
        # TODO: refresh button
        refresh = Button(self.app, text='Refresh', bg='#fff', command=self.refresh)
        refresh.place(x=0, y=0)
        self.listbox = Listbox(self.app, width=200, height=800, font=14)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)
        self.listbox.place(x=0, y=28)
        list_del_btn = Button(self.app, text="Delete", bg='#fff', command=self.list_delete)
        list_del_btn.place(x=50, y=0)
        for item in os.listdir():
            if item.endswith('.db'):
                self.listbox.insert(END, item)
        frame2 = Frame(self.app, bg='#f23', width=800, height=800)
        frame2.grid(row=0, column=1, sticky='NW')
        frame2.grid_propagate(0)
        frame2.update()
        self.listbox1 = Listbox(self.app, width=200, height=800, bg='#fff', font=14)
        self.listbox1.place(x=800, y=30)
        self.listbox1.bind('<<ListboxSelect>>', self.on_select1)
        self.table = Label(self.app, text='Tables', font=20, bg='#fff')
        self.table.place(x=800, y=0, width=200)
        db_name = StringVar
        db_label = Label(self.app, text='Subject Name', bg='#f23')
        db_label.place(x=210, y=10)
        self.db_entry = Entry(self.app, textvariable=db_name, width=35)
        self.db_entry.place(x=300, y=10)
        db_btn = Button(self.app, text='Create', bg='#fff', command=self.create_db)
        db_btn.place(y=10, x=550)
        # TODO: Table Creation
        table_name = StringVar
        table_label = Label(self.app, text='Question Type', bg='#f23')
        table_label.place(x=210, y=50)
        self.table_entry = Entry(self.app, textvariable=table_name, width=35)
        self.table_entry.place(x=300, y=50)
        table_btn = Button(self.app, text='Create', bg='#fff', command=self.create_table)
        table_btn.place(y=50, x=550)

        self.app.mainloop()

    # TODO: function defined here:
    def create_db(self):
        self.database = Database(self.db_entry.get() + '.db')
        self.refresh()

    def create_table(self):
        self.database.create_table(self.table_entry.get())
        self.show_tables()

    def refresh(self):
        self.listbox.delete(0, END)
        for item in os.listdir():
            if item.endswith('.db'):
                self.listbox.insert(END, item)

    def list_delete(self):
        Database(self.listbox.get(0))
        os.remove(self.listbox.get(ANCHOR))
        self.listbox.delete(ANCHOR)

    def on_select(self, evt):
        w = evt.widget
        b = self.listbox.get(ANCHOR)
        self.table.config(text=b)
        self.database = Database(b)
        self.show_tables()

    def on_select1(self, evt):
        w = evt.widget
        data = self.listbox1.get(ANCHOR)

        t1 = Label(self.app, text=data.upper(), bg='#f23', font=font.Font(size=30), fg='#fff')
        t1.place(x=300, y=100, width=400, height=50)
        self.t1_text = Text(self.app)
        self.t1_text.place(x=300, y=150, width=400, height=500)
        t1_btn = Button(self.app, text='Save', command=self.insert_data)
        t1_btn.place(x=300, y=700, width=100, height=40)

    def insert_data(self):
        data = []
        tag = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)', '(g)', '(h)', '(i)', '(j)', '(k)', '(l)']
        d = self.t1_text.get('1.0', 'end')

        print(d.split('\n'))

    def show_tables(self):
        self.listbox1.delete(0, END)
        for item in self.database.show_tables():
            self.listbox1.insert(END, item[0])


if __name__ == "__main__":
    QuestionOrganizer()
