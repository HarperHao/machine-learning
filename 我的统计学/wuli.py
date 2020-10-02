import numpy as np

# a = []
# b = []
# _ = input("请输入20个I，以逗号分隔开：")
# temp = _.split(',')
# a = list(map(float, temp))
# c = input("请输入20个U，以逗号分隔开：")
# temp = _.split(',')
# b = list(map(float, temp))
#
# I = np.array(a)
# U = np.array(b)
# R = U * 1000 / I
# P = U * I
#
# print(R)
# print("界线")
# print(P)

I=np.array([15.0,15.0,15.0,14.9,14.5,13.7,12.9,12.1,11.4,10.8,10.2,9.7,9.3,8.8,8.4,8.1,7.8,7.5,7.2,6.9])
print(len(I))
U=np.array([0.16,0.31,1.36,1.51,1.61,1.66,1.69,1.72,1.73,1.75,1.76,1.77,1.78,1.78,1.79,1.81,1.82,1.82,1.83,1.83])
print(len(U))
R=U*1000/I
P=U*I

print(R)
print('******')
print(P)
