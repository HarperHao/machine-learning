# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:11:30 2020

@author: maer
"""

import numpy as np

def LU_fenjie(A):
    n = len(A[0])
    L = np.zeros([n,n])
    U = np.zeros([n, n])
    for i in range(n):
        L[i][i] = 1
        #第一行特殊处理
        if i == 0:
            U[0][0] = A[0][0]
            for j in range(1,n):
                U[0][j] = A[0][j]
                L[j][0] = A[j][0]/U[0][0]
        else:
                #求U
                for j in range(i, n):
                    temp=0
                    for k in range(0, i):
                        temp = temp+L[i][k] * U[k][j]
                    U[i][j]=A[i][j]-temp
                #求L
                for j in range(i+1, n):
                    temp = 0
                    for k in range(0, i ):
                        temp = temp + L[j][k] * U[k][i]
                    L[j][i] = (A[j][i] - temp)/U[i][i]
    return L,U
            

A=[[2,-1,3],[3,2,-2],[6,4,3]]
L,U=LU_fenjie(A)
print(L,'\n',U)
L=np.mat(L)
U=np.mat(U)
L_n = L.I
U_n = U.I
B = np.dot(U_n,L_n).tolist()
print(B)
