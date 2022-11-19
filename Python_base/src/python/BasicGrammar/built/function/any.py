"""
any(iterable) 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。

元素除了是 0、空、FALSE 外都算 TRUE。
"""

print(any(['a', 'b', 'c', 'd']))
print(any(['a', False, 'c', 'd']))
print(any([0, '', False]))
print(any([]))