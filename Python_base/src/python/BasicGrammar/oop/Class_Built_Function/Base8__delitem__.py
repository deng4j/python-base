"""
__delitem__：中括号删除时触发
"""


class Foo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __delitem__(self, key):
        print('delattr执行，删除属性{}'.format(key))
        self.__dict__.pop(key)


foo = Foo("sb", 18)
del foo['age']
