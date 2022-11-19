"""
__delattr__：删除属性的时候会触发
"""


class Foo:

    def __init__(self, x):
        self.x = x

    def __delattr__(self, name: str) -> None:
        super().__delattr__(name)
        print("删除属性：", name)


foo = Foo(10)

del foo.x

try:
    print(foo.x)
except AttributeError as e:
    print(e)
