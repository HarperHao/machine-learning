"""
编写一个while 循环,提示用户输入其名字。
用户输入其名字后,在屏幕上打印一句问候语,
并将一条访问记录添加到文件guest_book.txt中。
确保这个文件中的每条记录都独占一行。此外设置当输入q时停止本程序。
"""


def fun():
    name = input("请输入名字：")
    while name != 'q':

        print("hello!{}".format(name))
        record =name+' has visited'
        with open(r'guest_book.txt', 'a') as f:
            f.write(record + '\n')

        name = input("请输入名字：")

fun()
