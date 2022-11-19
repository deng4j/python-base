"""
__delete__()：删除描述符时触发
"""


class Foo:

    def __init__(self, name):
        self.name = name

    def __delete__(self, instance):
        # self指当前实例；instance是调用者实例
        print("__delete__：{}  {}".format(self, instance))
        print(instance.__dict__)


class Boo:
    f = Foo("foo-1")


boo = Boo()
del boo.f

print(boo.f.name)
