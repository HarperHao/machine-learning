def binartInsert(a):
    # 折半插入排序，从小到大
    for i in range(1, len(a)):
        index = a[i]
        low = 0
