def div(x, y):
   try:
       print(x/y)
   except ZeroDivisionError:
       print("除数不能为0")
   except TypeError:
       print('必须为数值类型才能相除')
   else:
       print("没有错误")
   finally:
       print("程序结束运行")

div(3,4)