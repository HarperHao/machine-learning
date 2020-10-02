n=-1
while n<=1:
    n=eval(input("Please input the number you whant to generate arrangement:"))
    if n<=1:
        print("please input another number!")
else:
    print("inupt succeed!")
arrangement=[ i for i in range(1,n+1)]
arrangementTarget=[i for i in range(n,0,-1)]
print(arrangement)
while arrangement != arrangementTarget:
    for i in range(n-2,-1,-1):
        if arrangement[i] < arrangement[i+1] :
            for j in range(n-1,i,-1):
                if arrangement[j] > arrangement[i]:
                    arrangement[j],arrangement[i]=arrangement[i],arrangement[j]
                    break
            left= i+1
            right=n-1
            while left != right and left< right:
                arrangement[left],arrangement[right]=arrangement[right],arrangement[left]
                left+=1
                right-=1
            print(arrangement)
            break