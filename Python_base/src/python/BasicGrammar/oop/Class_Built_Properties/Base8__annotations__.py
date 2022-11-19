"""
__annotations__属性只包含形参和返回值的注解，即使在函数体中有类似的注解，但这并不等价于C语言中的变量声明，
    这样的注解不会创建变量，也不会被收集到这个特殊属性__annotations__中。
"""


class Base:
    a: int = 3
    b: str = 'abc'


class Derived(Base):
    pass


class Coo(Base):
    a: int = 4


print(Derived.__annotations__)
print(Coo.__annotations__)
