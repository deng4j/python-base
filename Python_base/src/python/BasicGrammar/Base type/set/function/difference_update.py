"""
set.difference_update(set)：移除set中两个集合中都存在的元素。
"""

x = {"apple", "banana", "cherry"}
y = {"apple", "microsoft", "google"}

x.difference_update(y)

print(x)
print(y)
