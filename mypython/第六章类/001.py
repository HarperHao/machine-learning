"""
自定义一个集合类
"""


class MySet:
    def __init__(self, data=None):
        if data == None:
            self.__data = []
        else:
            if not hasattr(data, '__iter__'):
                raise Exception('必须是可迭代的')
            temp = []
            for item in data:
                hash(item)
                if not item in temp:
                    temp.append(item)
            self.__data = temp

    def __del__(self):
        del self.__data

    def add(self, value):
        hash(value)
        if value not in self.__data:
            self.__data.append(value)
        else:
            print("元素已经存在，不会向集合中添加此元素")

    def remove(self, value):
        if value in self.__data:
            self.__data.remove(value)
            print("删除成功")
        else:
            print("此元素不存在，删除操作忽略")

    def pop(self):
        if not self.__data:
            print("集合已空，弹出操作忽略")
            return
        else:
            return self.__data.pop()

    def __sub__(self, anotherSet):
        if not isinstance(anotherSet, MySet):
            raise Exception('类型错误')
        result = MySet()
        for item in self.__data:
            if item not in anotherSet.__data:
                result.__data.append(item)
        return result

    def difference(self, anotherSet):
        return self - anotherSet

    def __or__(self, anotherSet):
        if not isinstance(anotherSet, MySet):
            raise Exception('类型错误')
        result = MySet(self.__data)
        for item in anotherSet.__data:
            if item not in result.__data:
                result.__data.append(item)
        return result

    def union(self, anotherSet):
        return self | anotherSet

    def __and__(self, anotherSet):
        if not isinstance(anotherSet, MySet):
            raise Exception('类型错误')
        result = MySet()
        for item in self.__data:
            if item in anotherSet.__data:
                result.__data.append(item)
        return result

    def __xor__(self, anotherSet):
        return (self - anotherSet) | (anotherSet - self)

    def symetric_difference(self, anotherSet):
        return self ^ anotherSet

    def __eq__(self, anotherSet):
        if not isinstance(anotherSet, MySet):
            raise Exception('类型错误')
        if sorted(self.__data) == sorted(anotherSet.__data):
            return True
        return False

    def __gt__(self, anotherSet):
        if not isinstance(anotherSet, MySet):
            raise Exception('类型错误')
        if self != anotherSet:
            flag1 = True
            for item in self.__data:
                if item not in anotherSet.__data:
                    flag1 = False
                    break
            flag2 = True
            for item in anotherSet.__data:
                if item not in self.__data:
                    flag2 = False
                    break
            if not flag1 and flag2:
                return True
            return False

    def __ge__(self, anotherSet):
        if not isinstance(anotherSet, Set):
            raise Exception('类型错误')
        return self == anotherSet or self > anotherSet

        # 提供方法，判断当前集合是否为另一个集合的真子集

    def issubset(self, anotherSet):
        return self < anotherSet

        # 提供方法，判断当前集合是否为另一个集合的超集

    def issuperset(self, anotherSet):
        return self > anotherSet

        # 提供方法，清空集合所有元素

    def clear(self):
        while self.__data:
            del self.__data[-1]
        print('集合已清空')

        # 运算符重载，使得集合可迭代

    def __iter__(self):
        return iter(self.__data)

        # 运算符重载，支持in运算符

    def __contains__(self, value):
        return value in self.__data

        # 支持内置函数len()

    def __len__(self):
        return len(self.__data)

        # 直接查看该类对象时调用该函数

    def __repr__(self):
        return '{' + str(self.__data)[1:-1] + '}'

        # 使用print()函数输出该类对象时调用该函数

    __str__ = __repr__
