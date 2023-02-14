"""
copy() 函数用于浅拷贝列表，类似于 a[:]。
"""

list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list2 = list1.copy()
print("list2 列表: ", list2)

print("list1[0]：{}".format(id(list1[0])))
print("list2[0]：{}".format(id(list2[0])))
