from BasicGrammar.oop.Class_Built_Properties.__module__.mod import C

"""
__module__ 表示当前操作的对象在那个模块
"""


class Foo:
    pass


print("本模块__module__：", Foo.__module__)

c = C()
print("mod模块__module__：", c.__module__)
