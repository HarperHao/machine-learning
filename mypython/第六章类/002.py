"""
python属性
"""


class Test:
    def __init__(self, value):
        self.__value = value

    def __get(self):
        return self.__value

    def __set(self, v):
        self.__value = v

    def __del(self):
        del self.__value

    value = property(__get, __set, __del)


t = Test(2)
print(t.value)
t.value = 3
print(t.value)
del t.value
#print(t.value)
