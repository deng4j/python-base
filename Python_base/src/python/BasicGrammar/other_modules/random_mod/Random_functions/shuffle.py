import random

"""
shuffle() 方法将序列的所有元素随机排序。
"""

list1 = [20, 16, 10, 5]
random.shuffle(list1)
print("随机排序列表 : ", list1)

list1 = [[0, 0], [1, 1], [2, 2]]
random.shuffle(list1)
print("随机排序列表 : ", list1)
