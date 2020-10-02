import random
import string
def get_seq(n):
    x = string.ascii_letters + string.digits + string.punctuation#包含字母大小写、数字、标点符号
    y = [random.choice(x) for i in range(n)]
    return y
def arr_sort(arr,n):
    lists = arr[:n+1]
    m = arr[n+1:]
    m.sort()
    lists.extend(m)
    return lists

def per(arr):
    if arr == sorted(arr,reverse=True):
        return
    for i in range(len(arr)-1,-1,-1):
        if arr[i] > arr[i-1]:
            index1 = i - 1
            break
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > arr[index1]:
            temp2 = arr[i]
            index2 = i
            break
    arr[index2] = arr[index1]
    arr[index1] = temp2
    arr = arr_sort(arr,index1)
    print(arr)
    per(arr)


if __name__ == "__main__":
    n = int(input("请输入有多少个元素:"))
    arr = get_seq(n)
    arr.sort()
    print(arr)
    per(arr)