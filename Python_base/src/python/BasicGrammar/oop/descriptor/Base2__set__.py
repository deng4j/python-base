"""
__set__()：给描述器赋值时触发
"""


class Foo:

    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        # self指当前实例；instance是调用者实例；value是赋值的对象
        print("__set__：{}  {}  {}".format(self, instance, value))
        self.name = value


class Boo:
    f = Foo("foo-1")


boo = Boo()
boo.f = 10
print(boo.f.name)
