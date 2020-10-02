"""
请编写程序输入由“*”组成的空心菱形图案。要求：输入菱形的边数n，然后输出如右图所示的空心菱形图案。
要求使用最简短的代码完成。
"""
# 共2*n+1行
n = int(input("请输入行数："))
first_pos = 0
k = 2 * n + 1
# 第一部分
for i in range(1, 2 * (2 * n + 1)):
    if i == k:
        print('*')
    else:
        print(' ', end='')
# 第二部分

for j in range(2, n + 1):
    # 每行总共有这么多位置
    for i in range(1, 2 * (2 * n + 1)):
        if i == (k - (j - 1) * 2):#5
            print('*', end='')
        elif i == (2 * (2 * n + 1) - first_pos):
            print('*')
        else:
            print(' ', end='')
    first_pos = 0
