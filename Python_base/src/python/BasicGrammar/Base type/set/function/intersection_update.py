"""
set.intersection_update(set1, set2 ... etc)：移除set中不是多个集合的交集的元素。
"""

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)

print(x)
