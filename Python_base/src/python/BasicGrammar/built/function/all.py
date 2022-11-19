"""
all(iterable)：用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。元素除了是 0、空、None、False 外都算 True。
"""

print(all(['a', 'b', 'c', 'd']))
print(all([0, 1, 2, 3]))
print(all([]))
