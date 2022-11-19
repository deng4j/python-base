"""
__setattr__：添加/修改属性会触发它
"""


class Foo:

    def __init__(self, x):
        self.x = x

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        print("设置属性：", key, "--", value)


foo = Foo(10)

foo.x = 20
