"""
callable(object)：用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；
    但如果返回 False，调用对象 object 绝对不会成功。

对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True。
"""


def add(a, b):
    return a + b


print(callable(add))

print("---------------------------------------------------")


class A:
    pass


print(callable(A))

print(callable(A()))

print("---------------------------------------------------")


class B:
    def __call__(self):
        return 0


print(callable(B))
print(callable(B()))
