"""
set.union(set1, set2...)：返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次。
"""

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

union = x.union(y, z)

print(union)
