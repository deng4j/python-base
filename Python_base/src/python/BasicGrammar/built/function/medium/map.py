print("------ map() ------")
"""
map(function, iterable, ...) 会根据提供的函数对指定序列做映射。
    function - 针对每一个迭代调用的函数
    iterable - 支持迭代的一个或者多个对象。
"""

a, b, c = map(int, ["1", "2", "3"])
print("映射后：", a, b, c)
