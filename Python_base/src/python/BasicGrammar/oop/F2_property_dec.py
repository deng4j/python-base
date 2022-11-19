"""
经典装饰器方式property()：
    1.第一个参数是方法名，调用 对象.属性 时自动触发执行方法
    2.第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法
    3.第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法
    4.第四个参数是字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息
"""


class Foo:

    def get_prop(self):
        print("get_prop(self)")

    def set_prop(self, value):
        print("set_prop(self)")

    def del_prop(self):
        print("del_prop(self)")

    # 经典装饰器方式
    PROP = property(get_prop, set_prop, del_prop, "doc：经典装饰器")


print("----------------- 经典装饰器方式1 ------------------")

foo_obj = Foo()
foo_obj.PROP  # 调用property属性

print("----------------- 经典装饰器方式2 ------------------")

foo_obj.PROP = 121

print("----------------- 经典装饰器方式3 ------------------")

print(Foo.PROP.__doc__)

print("----------------- 经典装饰器方式4 ------------------")

del foo_obj.PROP
