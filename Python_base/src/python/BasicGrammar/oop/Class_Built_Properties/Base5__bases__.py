"""
obj.__bases__：返回所有的父类，隐性继承objecr类。一个类除了object之外没有继承其他类，则会返回object。
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
    print(Aoo.__bases__)
    print(Boo.__bases__)
    print(Coo.__bases__)
    print(Coo.__base__)
