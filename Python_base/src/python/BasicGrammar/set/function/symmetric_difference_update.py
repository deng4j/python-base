"""
set.symmetric_difference_update(set)：移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
"""

x = {"a", "b", "c"}
y = {"c", "d", "e"}
x.symmetric_difference_update(y)

print(x)
