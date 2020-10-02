from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creatWidget()

    def creatWidget(self):
        self.button = Button(self)
        self.button["text"] = "你好"
        self.button.pack()
        self.button["command"] = self.hello

        self.quit_button = Button(master=self, text="退出", command=root.destroy)
        self.quit_button.pack()
        self.photo = PhotoImage(file=r'E:\123.gif')
        self.button1 = Button(self, text="study",image=self.photo, command=self.hello)
        self.button1.pack()

    def hello(self):
        messagebox.showinfo("你好", "hello,python")


root = Tk()
root.geometry("640x480+200+300")
app = Application(root)
root.mainloop()
