import random
def dict_sort(lis):
    c=1
    while(True):
        i=0
        d=0
        k=0
        for x in range(-2,-len(lis)-1,-1):
            if lis[x] <lis[x+1] :
                i=x
                d=lis[x+1]-lis[x]
                k=x+1
                break
        if i==0:
            break
        elif i!=0  :
            for x in range(-1, i , -1):
                if lis[i] < lis[x ] and d>lis[x]-lis[i]:
                    d=lis[x]-lis[i]
                    k=x
            lis[k],lis[i] = lis[i],lis[k]
            print('i=',i,'k=',k)
            if (-1-i)>1:
                t=i+1
                tt=-1
                for x in range((-1-i)//2):
                    lis[t],lis[tt] = lis[tt],lis[t]
                    t=t+1
                    tt=tt-1
        for _ in range(len(lis)):
            print(lis[_], end=' ')
        print('', end=' ')
        c=c+1
    print('排列个数：',c)
def main():
    n=int(input('输入n:'))
    if n<=0:
        print("排列数：0")
    else :
        lis = [random.randint(1,100) for x in range(n)]
        lis.sort()
        for _ in range(len(lis)):
            print(lis[_], end=' ')
        print('',end=' ')
        dict_sort(lis)
if __name__ == '__main__' :
    main()