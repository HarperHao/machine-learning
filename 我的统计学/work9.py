import numpy as np

t = np.array([1 / 4, 1 / 4, 1 / 4, 1 / 4])
Q = np.array([[1 / 3, 1 / 3, 1 / 3, 0],
              [0, 0, 1 / 2, 1 / 2],
              [0, 1, 0, 0],
              [1 / 2, 0, 0, 1 / 2]
              ])
temp = np.dot(Q, Q)
for i in range(100 - 2):
    temp = np.dot(temp, Q)
print(np.dot(t, temp))
# [0.21428571 0.28571429 0.21428571 0.28571429]
