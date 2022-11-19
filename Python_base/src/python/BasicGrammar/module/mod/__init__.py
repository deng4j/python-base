from BasicGrammar.module.mod.mod1 import *

"""
在Python工程里，当python检测到一个目录下存在__init__.py文件时，python就会把它当成一个模块(module)。
"""


def f1():
    print("__init__.py  f1()")


def f2():
    print("__init__.py  f2()")


__all__ = ["f1", 'fmod1']
