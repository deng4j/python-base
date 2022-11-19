"""
set.difference(set)：用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中。
"""

x = {"apple", "banana", "cherry"}
y = {"apple", "microsoft", "google"}

z = x.difference(y)

print(z)
