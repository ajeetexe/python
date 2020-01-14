from tkinter import *
from tkinter import messagebox
import json
from difflib import get_close_matches


class Dictionary:
    # database of dictionary
    data = json.load(open('data.json'))
    
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.dictionary.title("Dictionary")
        self.dictionary.resizable(0, 0)
        f = Frame(dictionary, bg='#fff', width=500, height=200)
        f.grid(row=0, column=0, sticky="NW")
        f.grid_propagate(0)
        f.update()
        label = Label(
            dictionary, text="Type Your  Word and Press Enter Key:", bg="#fff", fg="#FF4500")
        label.place(x=10, y=10)
        self.enter_value = StringVar()
        self.entry = Entry(dictionary, textvariable=self.enter_value, width=40)
        self.entry.place(x=250, y=10)
        self.entry.focus()
        self.entry.bind('<Return>', lambda func1: self.execute())
        self.text = Text(dictionary, width=58, height=8)
        self.text.place(x=10, y=40)

    def execute(self):
        data = self.func(self.entry.get())
        self.text.config(state="normal")
        self.text.delete(1.0, END)
        self.text.insert(END, data)
        self.text.config(state="disabled")
   
    def func(self,args):
        args = args.title()
        if args in self.data:
            return self.data[args]
        elif len(get_close_matches(args, self.data.keys())) > 0:
            yesOrno = messagebox.askyesno("Available Word", 'Did you mean {} instead:- '.format(get_close_matches(args, self.data.keys())[0]))
            if yesOrno == True:
                self.enter_value.set(get_close_matches(args, self.data.keys())[0])
                return self.data[get_close_matches(args, self.data.keys())[0]]
            elif yesOrno == False:
                return 'The word you searching not exists in our storage'
            else:
                return "We don't understand your entry"
        else:
            return "The word does't exit, We are really sorry!!!"


def run():
    dictionary = Tk()
    Dictionary(dictionary)
    dictionary.mainloop()


if __name__ == "__main__":
    run()
