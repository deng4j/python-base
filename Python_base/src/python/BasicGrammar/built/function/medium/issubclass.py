"""
issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类。
"""


class Parent:
    pass


class Parent1:
    pass


class Sub(Parent):
    pass


print(issubclass(Sub, Parent))
print(issubclass(Parent, Parent))
print(issubclass(Parent, object))
print(issubclass(Sub, object))

print(issubclass(Sub, Parent1))
