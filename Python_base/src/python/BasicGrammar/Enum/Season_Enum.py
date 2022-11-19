from enum import Enum

"""
Enum(name,iterable)：
    name：枚举名
    iterable：可迭代对象
"""

# 创建枚举2
Season = Enum('Season', ['spring', 'summer', 'autumn', 'winter'])

print(Season.spring)
print(type(Season.spring))
print(Season.spring.name)
print(Season.spring.value)

print("----------------------------------------------------")

Season1 = Enum('Season1', {'spring': 2, 'summer': 3, 'autumn': 4, 'winter': 5})

print(Season1.spring.value)
