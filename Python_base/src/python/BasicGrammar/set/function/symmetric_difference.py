"""
set.symmetric_difference(set)：返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素。
"""

x = {"a", "b", "c"}
y = {"c", "d", "e"}
difference = x.symmetric_difference(y)

print(difference)
