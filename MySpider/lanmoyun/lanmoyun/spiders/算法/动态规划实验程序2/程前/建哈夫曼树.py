ls=[]
print ('输入构建哈夫曼树的节点值(输入0停止输入):')
while 1:
    n=int(input())
    if n==0:
        break
    ls.append(n)

print("构建哈夫曼树如下:")
while len(ls)>=2:
    ls.sort()
    print("h1=%d \t h2=%d \t h1+h2=%d"%(ls[0],ls[1],ls[0]+ls[1]))
    ls.append(ls[0]+ls[1])
    ls.pop(0)
    ls.pop(0)