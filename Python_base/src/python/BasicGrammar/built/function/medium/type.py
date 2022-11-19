"""
class type(object) 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。

注意：type()不会认为子类是一种父类类型，不考虑继承关系。
"""


class Foo(object):
    pass


class Bar(Foo):
    pass


print(type('foo') == str)

print(type(2.3) in (int, float))

print(type(Bar()) == Foo)

print(type(Bar()) == Bar())
