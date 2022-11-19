from typing import Any

"""
__init__(self)：当实例对象创建之后被调用
__new__(cls)：实例对象创建之前被调用，new() 函数只能用于从Object继承的新式类。

调用顺序：
    1.__new__在__init__之前被调用
    2.__new__的返回值（实例）将传递给__init__方法的第一个参数self
"""


class Foo:
    x = None

    def __init__(self):
        self.x = 5
        print("__int__(self)")

    def __new__(cls) -> Any:
        print("__new__(cls)")
        return super().__new__(cls)


foo = Foo()
print(foo.x)
