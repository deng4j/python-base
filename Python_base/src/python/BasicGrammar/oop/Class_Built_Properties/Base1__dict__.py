"""
__dict__：该属性可以用类名或者类的实例对象来调用，用类名直接调用 __dict__，会输出该由类中所有类属性组成的字典；
    而使用类的实例对象调用 __dict__，会输出由类中所有实例属性组成的字典。
"""


class People:
    pname = "pppp"

    def __init__(self, p):
        self.p = p


class Foo(People):

    def __init__(self, f):
        self.f = f


foo = Foo(10)
print(foo.__dict__)
print(Foo.__dict__)
