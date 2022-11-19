"""
返回列表的索引和值，增加代码可读性。
"""

print("---------------------------- list -------------------------------")

lst = ['a', 'b', 'c', 'd']

for index, item in enumerate(lst):
    print("{} --  {}".format(index, item))

print("---------------------------- dict -------------------------------")

dic = {'k1': 1, 'k2': 6, 'k3': 7, 'k4': 8}

for index, item in enumerate(dic):
    print("{} --  {}".format(index, item))
