"""计算器界面"""
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.pack()
        self.creatWidget()

    def creatWidget(self):
        Entry(self).grid(row=0, column=0, columnspan=4)
        text = (
            ('(', ')', '%', 'C'),
            (7, 8, 9, '/'),
            (4, 5, 6, 'x'),
            (1, 2, 3, '-'),
            (0, '.', '=', '+')
        )
        for rindex, r in enumerate(text):
            for cindex, c in enumerate(r):
                Button(self, text=c,width=2). \
                    grid(row=rindex+1, column=cindex,sticky=NSEW)


root = Tk()
app = Application(root)
root.geometry("200x200+200+200")
root.mainloop()
