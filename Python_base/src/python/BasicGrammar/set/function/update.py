"""
set.update(set1)：取并集，将结果保存在set中
"""

x = {"a", "b", "c"}
y = {"f", "d", "a"}

x.update(y)

print(x)
print(y)
