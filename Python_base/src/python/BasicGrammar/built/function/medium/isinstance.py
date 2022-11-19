"""
isinstance()：判断某个对象是不是某个类的实例，会认为子类是一种父类类型，考虑继承关系。

如果要判断两个类型是否相同推荐使用 isinstance()。
"""


class Foo(object):
    pass


class Bar(Foo):
    pass


print(isinstance(Bar(), Foo))

print(isinstance(Bar, Foo))

print(isinstance(Foo, Bar))

print(isinstance(Foo(), Foo))
print(isinstance(Foo, Foo))

print("-------------------注意点⚠️-------------------")

"""
类本身也是对象，对象a对应的类和类B是create_class函数返回的两个不同的对象，存在于不同的内存地址中。
"""


def create_class(cls_name: str):
    return type(cls_name, (), dict())


a = create_class("MyClass")
B = create_class("MyClass")
print(type(a))
print(B)
print(isinstance(a, B))

print("---------------------------------------")

f = create_class("Foo")
print(type(f))
print(Foo)
print(isinstance(f, Foo))
