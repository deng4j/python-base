"""
__call__：对象后面加括号时，触发执行。
作用：把类实例变成一个可调用对象。
"""


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        print('__call__触发：{}  {}'.format(args, kwargs))


p = People('egon', 18)

p("大傻逼", "什么鬼！", speak="你在叫什么")
