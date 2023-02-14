"""
set.issubset(set)：判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False。
"""

x = {"a", "b", "c"}
y = {"a", "b", "c", "d"}

print(x.issubset(y))
