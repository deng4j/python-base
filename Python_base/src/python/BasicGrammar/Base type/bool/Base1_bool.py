"""
Python中所有数据类型的值自带布尔值。如此多的数据类型中只需要记住只有0、None、空、False的布尔值为False，其余的为True。
"""

print(type(True))
print(True)

print("---------------- -----------------")

print(bool(0))
print(bool('nick'))
print(bool(1 > 2))
print(bool(1 == 1))

print("---------------- -----------------")

print(bool(0))
print(bool(None))
print(bool(''))
print(bool([]))
print(bool([1]))
print(bool({}))
print(bool(False))
