"""模仿实际的记事本，并实现相应的功能"""
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.colorchooser import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.textpad = None
        self.pack()
        self.createWidget()

    def createWidget(self):
        menubar = Menu(self.master)

        # 子菜单
        menuFile = Menu(menubar)
        menuEdit = Menu(menubar)
        menuHelp = Menu(menubar)
        # 子菜单加到菜单栏中
        menubar.add_cascade(label="文件(F)", menu=menuFile)
        menubar.add_cascade(label="编辑(E)", menu=menuEdit)
        menubar.add_cascade(label="帮助(H)", menu=menuHelp)
        # 菜单添加到菜单项
        menuFile.add_command(label="新建", accelerator='ctrl+n', command=self.newFile)
        menuFile.add_command(label="打开", accelerator='ctrl+o', command=self.openFile)
        menuFile.add_command(label='保存', accelerator='ctrl+s', command=self.saveFile1)
        menuFile.add_command(label='另存为', accelerator='ctrl+shift+s', command=self.saveFile2)
        menuFile.add_separator()
        menuFile.add_command(label="退出", accelerator="ctrl+q", command=self.Quit)
        menuHelp.add_command(label='版本', command=self.helpInfo)
        menuEdit.add_command(label='撤销', command=self.undo)
        root["menu"] = menubar
        # 帮助栏

        # 文本编辑区
        self.textpad = Text(root, width=640, height=480, undo=True, autoseparators=False)
        self.textpad.pack()

        # 上下文菜单
        self.contextMenu = Menu(root)
        self.contextMenu.add_command(label="背景颜色", command=self.colorChange)

        root.bind("<Button-3>", self.createContextMenu)

        # 快捷键处理
        root.bind("<Control-n>", lambda event: self.newFile())
        root.bind("<Control-s>", lambda event: self.saveFile1())
        root.bind("<Control-o>", lambda event: self.openFile())
        root.bind("<Control-q>", lambda event: self.Quit())
        root.bind("<Control-Shift-KeyPress-s>", lambda event: self.saveFile2())
        # root.bind("<KeyPress-9>", lambda event: self.undo())#快捷键没反应
        self.textpad.bind('<Key>', self.callback)
        self.filename = ''

    def newFile(self):
        self.textpad.delete(1.0, END)
        self.filename = asksaveasfilename(title='新建', initialfile='未命名.txt',
                                          filetypes=[('文本文档', '*.txt')],
                                          defaultextension='.txt')

    def openFile(self):
        self.textpad.delete(1.0, END)
        with askopenfile(title='打开') as f:
            self.textpad.insert(INSERT, f.read())
        self.filename = f.name

    def saveFile1(self):
        if self.filename == '':
            self.saveFile2()
        else:
            with open(self.filename, 'w') as f:
                f.write(self.textpad.get(1.0, END))

    def saveFile2(self):
        self.filename = asksaveasfilename(title='另存为', initialfile='未命名.txt',
                                          filetypes=[('文本文档', '*.txt')],
                                          defaultextension='.txt')

    def Quit(self):
        root.quit()

    def helpInfo(self):
        messagebox.showinfo(title="Message", message="Version-1.0   by HarperHao")

    def createContextMenu(self, event):
        self.contextMenu.post(event.x_root, event.y_root)

    def colorChange(self):
        c = askcolor(title='选择背景颜色', color='red')
        self.textpad['bg'] = c[1]

    def undo(self):
        self.textpad.edit_undo()

    def callback(self, event):
        self.textpad.edit_separator()


root = Tk()
root.geometry("640x480+200+300")
app = Application(root)
root.mainloop()
