"""
set.intersection(set1, set2 ... etc)：返回多个集合的交集。
"""

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)
