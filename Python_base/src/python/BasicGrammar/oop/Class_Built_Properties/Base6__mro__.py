"""
obj.__mro__：返回继承顺序
"""


class Aoo:
    pass


class Boo(Aoo):
    pass


class Boo1:
    pass


class Coo(Boo, Boo1):
    pass


if __name__ == '__main__':
    print(Aoo.__mro__)
    print(Boo.__mro__)
    print(Coo.__mro__)
