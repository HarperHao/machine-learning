import numpy as np
weight = [2, 2, 6, 5, 4]#重量
value = [3, 6, 5, 4, 6]#价值
weight_most = 10#最大容量
def bag_0_1(weight, value, weight_most):  # return max value
    num = len(weight)
    weight.insert(0, 0)
    value.insert(0, 0)
    bag = np.zeros((num + 1, weight_most + 1), dtype=np.int32)
    for i in range(1, num + 1):
        for j in range(1, weight_most + 1):
            if weight[i] <= j:
                bag[i][j] = max(bag[i - 1][j - weight[i]] + value[i], bag[i - 1][j])
            else:
                bag[i][j] = bag[i - 1][j]
    return bag
result = bag_0_1(weight, value, weight_most)
print(result)
print('最大的价值是:',result[-1][-1])