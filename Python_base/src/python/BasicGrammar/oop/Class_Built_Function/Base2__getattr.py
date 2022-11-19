"""
__getattr__：当实例对象访问不存在的属性时调用
"""


class Foo:

    def __init__(self, x):
        self.x = x

    def __getattr__(self, name):
        print("属性查找失败:", name)


foo = Foo(10)
print(foo.x)
foo.y
