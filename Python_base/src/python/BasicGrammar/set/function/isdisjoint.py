"""
set.isdisjoint(set)：判断是否有交集。没有返回True，有则返回False。
"""

x = {"a", "b", "c"}
y = {"c", "d", "e"}

print(x.isdisjoint(y))
