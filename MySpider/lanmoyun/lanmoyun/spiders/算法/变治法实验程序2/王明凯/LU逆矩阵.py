import random
from decimal import Decimal
import math
def Mymult(a,b):
    #分数乘法
    resault=[a[0]*b[0],a[1]*b[1]]
    gc=math.gcd(resault[0],resault[1])
    resault[0],resault[1]=resault[0]//gc,resault[1]//gc
    return resault
def MyDivide(a,b):
    #分数除法
    resault=[a[0]*b[1],a[1]*b[0]]
    gc=math.gcd(resault[0],resault[1])
    resault[0],resault[1]=resault[0]//gc,resault[1]//gc
    return resault
def Myadd(a,b):
    #分数加法
    resault=[a[0]*b[1]+b[0]*a[1],a[1]*b[1]]
    gc=math.gcd(resault[0],resault[1])
    resault[0],resault[1]=resault[0]//gc,resault[1]//gc
    return resault
def Myreduce(a,b):
    #分数减法
    resault=[a[0]*b[1]-b[0]*a[1],a[1]*b[1]]
    gc=math.gcd(resault[0],resault[1])
    resault[0],resault[1]=resault[0]//gc,resault[1]//gc
    return resault
def operateOnce(A,B,n):
    #求一列
    L=[ [ [0,1] for j in range(n)] for i in range(n)]
    U=[[[k for k in j] for j in i] for i in A]
    for i in range(0,n):
        for j in range(i+1,n):
            L[j][i]=MyDivide(U[j][i],U[i][i])
            for k in range(0,n):
                U[j][k]=Myreduce(U[j][k],Mymult(U[i][k],L[j][i]))
    Y=[]
    for i in range(n):
        Sumbefor=[0,1]
        for j in range(i):
            Sumbefor=Myadd(Sumbefor,Mymult(L[i][j],Y[j]))
        Y.append(Myreduce(B[i],Sumbefor))
    X=[[0,1] for i in range(n)]
    for i in range(n-1,-1,-1):
        Sumbefor=[0,1]
        for j in range(i+1,n):
            Sumbefor=Myadd(Sumbefor,Mymult(U[i][j],X[j]))
        X[i]=MyDivide(Myreduce(Y[i],Sumbefor),U[i][i])
    return X
n=eval(input('请你输入方阵的行：'))
A=[[ [random.randint(0,100),1]  for j in range(n)] for i in range(n)]#矩阵A
B=[[ [0,1] for j in range(n)]  for i in range(n)]#单位矩阵
for i in range(n):
    B[i][i][0]=1#将对角上置为1
InverseA=[]
for i in range(n):
    InverseA.append(operateOnce(A,B[i],n))#最后要转置一下
for i in range(n):#转置
    for j in range(0,i):
        InverseA[i][j],InverseA[j][i]=InverseA[j][i],InverseA[i][j]
for i in range(n):#打印原矩阵
    for j in range(n):
        print(A[i][j][0],'/',A[i][j][1],end='\t') if A[i][j][1]!=1 else print(A[i][j][0],end='\t')
    print()
print('-----------------------------------')
for i in range(n):#打印逆矩阵
    for j in range(n):
        print(InverseA[i][j][0],'/',InverseA[i][j][1],end='\t') if InverseA[i][j][1]!=1 else print(InverseA[i][j][0],end='\t')
    print()