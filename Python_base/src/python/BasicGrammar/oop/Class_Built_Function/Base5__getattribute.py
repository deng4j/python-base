"""
__getattribute__：查找属性无论是否存在，都会执行。

当__getattribute__与__getattr__同时存在，只会执行__getattrbute__，除非__getattribute__在执行过程中抛出异常AttributeError
"""
from typing import Any


class Foo:

    def __init__(self, x):
        self.x = x

    def __getattribute__(self, name: str) -> Any:
        try:
            return super().__getattribute__(name)
        except:
            print("不存在属性：", name)
        else:
            print("__getattribute__", name)


foo = Foo(10)
print(foo.x)
print(foo.y)
