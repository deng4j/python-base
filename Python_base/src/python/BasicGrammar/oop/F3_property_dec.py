"""
类的装饰器:无参
"""


def decorate(cls):
    print('类的装饰器开始运行啦------>')
    return cls


@decorate
class Foo:
    pass


foo = Foo()
