"""
实现输出2-3+4-5+6...+100的和
"""
def fun():
    i = [k for k in range(2, 101) if k % 2 == 0]
    j = [-k for k in range(2, 101) if k % 2 == 1]
    print(sum(i) + sum(j))


fun()
