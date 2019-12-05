import sys

if __name__ == "__main__":
    list1 = sys.stdin.readline().strip()
    a = []
    dict = {}
    for data in list1:
        if data.isspace():
            continue
        else:
            a.append(data)
    for key in a:
        dict[key] = dict.get(key, 0) + 1
    b = list(dict.values())
    c = set(b)
    c = list(c)
    print(b)
    print(c)
    if (len(b) == len(c)):
        if (b.sort() == c.sort()):
            print(1)
    else:
        print(-1)
