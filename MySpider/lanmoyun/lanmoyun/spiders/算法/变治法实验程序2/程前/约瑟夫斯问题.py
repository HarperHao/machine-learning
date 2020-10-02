n=int(input("输入总人数："))
Q=int(input("输入规定退出的倍数："))
ls=[0]+[i for i in range(1,n+1)]
M=0
L=len(ls)-1
while L>1:
    i=1
    r=0
    m = (L+M)% Q
    while i<=L:
        if (i+M)%Q==0:
            ls.pop(i-r)
            r+=1
        i+=1
    print(ls)
    M=m
    L=len(ls)-1
print(ls[1])