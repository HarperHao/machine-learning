# x = {'A': [('B1', 8), ('B2', 12)], 'B1': [('C1', 4), ('C2', 5), ('C3', 7)], 'B2': [('C1', 6), ('C2', 7), ('C3', 8)],
#      'C1': [('D1', 6), ('D2', 5)], 'C2': [('D1', 4), ('D2', 3)], 'C3': [('D1', 3), ('D2', 2)], 'D1': [('E', 3)],
#      'D2': [('E', 5)]}
# print(x['A'])
a = []
for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)
for i in range(10):
     a[i][0]=1
     a[i][i]=1
for i in range(2,10):
     for j in range(1,i):
          a[i][j]=a[i-1][j-1]+a[i-1][j]
print(a)