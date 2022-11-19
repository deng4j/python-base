"""
描述符：描述符本质就是一个新式类，在这个新式类中，至少实现了__get__()，__set__()，__delete__()中的一个，这也被称为描述符协议
作用：代理一个类的属性，让程序员在引用一个对象属性时自定义要完成的工作；它是实现大部分Python类特性中最底层的数据结构的实现手段，
    是使用到装饰器或者元类的大型框架中的一个非常重要组件。

__get__()：调用描述符时触发
"""


class Foo:

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        # self指当前实例，调用者；Instance是owner的实例；Owner是属性所属的类。
        print('{}：：{}：：{}'.format(self, instance, owner))
        print(instance.__dict__)
        return self


class Boo:
    f = Foo("foo-1")

    def __init__(self, name):
        self.b = name


boo = Boo("boo-1")
print(boo.f.name)
