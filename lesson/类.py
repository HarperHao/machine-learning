class Test:
    def __init__(self, value):
        self.__value = value

    @property
    def x(self):
        return self.__value


t = Test(3)
print(t.x)
