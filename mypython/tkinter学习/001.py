from tkinter import *
from tkinter import messagebox

root = Tk()
button = Button(root)
button['text'] = 'lvhao'
button.pack()


def hello(e):
    messagebox.showinfo(title="Message",message="hello,python")


button.bind("<Button-1>", hello)

root.mainloop()
