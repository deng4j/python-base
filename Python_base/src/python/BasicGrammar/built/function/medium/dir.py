import sys

"""
dir()用于查找模块定义的名称。 它返回一个排序过的字符串列表。
    无参：返回当前本地作用域中的名称列表。
    有参：尝试返回该对象的有效属性列表。
        1.如果对象是模块对象，则列表包含模块的属性名称。
        2.如果对象是类型或类对象，则列表包含它们的属性名称，并且递归查找所有基类的属性。
        3.否则，列表包含对象的属性名称，它的类属性名称，并且递归查找它的类的所有基类的属性。
"""

print(dir(sys))
