from BasicGrammar.module.package_object.domain.Obj import Foo
from BasicGrammar.module.package_object.domain.GetObj import f, Boo

"""
同一个对象，通过不同路径导入，得到的对象不一样。
"""

print(Foo)
print(type(f))

print(isinstance(f, Foo))

print("----------------------------------------")

print(Boo)
print(Boo.__bases__)  # 查看父类
print(isinstance(Boo(), Foo))  # 测试继承关系
