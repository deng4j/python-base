"""
property装饰器用于将被装饰的方法伪装成一个数据属性，在使用时可以不用加括号而直接使用。
    1. 定义时，在实例方法的基础上添加 @property 装饰器；并且仅有一个self参数
    2. 调用时，无需括号

property属性内部进⾏⼀系列的逻辑计算，最终将计算 结果返回。
"""


class Foo:

    # 定义property属性
    @property
    def prop(self):
        print("@property prop(self)")

    @prop.setter
    def prop(self, value):
        print('@prop.setter')

    @prop.deleter
    def prop(self):
        print('@prop.deleter')


print("----------------- @property ------------------")

foo_obj = Foo()
foo_obj.prop  # 调用property属性

print("----------------- @prop.setter ------------------")

foo_obj.prop = 111

print("----------------- @prop.deleter ------------------")

del foo_obj.prop
