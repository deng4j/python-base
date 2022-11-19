"""
类的装饰器:有参
"""


def typeassert(**kwargs):
    def decorate(cls):
        print('类的装饰器开始运行啦------>', kwargs)
        return cls

    return decorate


@typeassert(
    name=str, age=int, salary=float
)
class Foo:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


foo = Foo('nick', 18, 3333.3)
