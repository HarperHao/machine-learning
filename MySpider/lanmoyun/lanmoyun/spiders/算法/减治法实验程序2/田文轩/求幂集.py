def transform(m,n):
    arr=[0]*m
    for i in range(m-1,-1,-1):
        arr[i]=int(n%2)
        n=int(n/2)
    return arr
str_=list(input("请输入集合元素（以空格隔开）：").split(" "))
length=len(str_)
for i in range(2**length):
    lst=transform(length,i)
    print("{",end="")
    count=lst.count(1)
    num=0
    for index,j in enumerate(lst):
        if j==1 and num<count-1:
            print(str_[index],end=",")
            num+=1
            continue
        if j==1 and num==count-1:
             print(str_[index],end="")
             num+=1
    print("}")
    print()
