from tkinter import *


root = Tk()

def insert():
    text = name_entry.get()
    Label(text = text).grid(row = 1, column = 0, columnspan = 2)

def clear():
    name_entry.delete(0, END)

def backspace():
    name_entry.delete(len(name_entry.get())-1,
                      END)

      
name_entry = Entry()
name_entry.grid(row=0, column=0)
#name_entry.insert(0, "Name")
name_entry.config(fg='#00ff00', bg='#111111',
                  font=('Ink Free', 28), width='50')

print_button = Button(text="Print", bg='#00ff00', fg='#111111',
                      width='10', padx='5', pady='5', command=insert)
print_button.grid(row=0, column=1)

clear_button = Button(text="Clear", bg='#00ff00', fg='#111111',
                      width='10', padx='5', pady='5', command=clear)
clear_button.grid(row=0, column=2)

backspace_button = Button(text="Backspace", bg='#00ff00', fg='#111111',
                      width='10', padx='5', pady='5', command=backspace)
backspace_button.grid(row=0, column=3)



root.mainloop()
