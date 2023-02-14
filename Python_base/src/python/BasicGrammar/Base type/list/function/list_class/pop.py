"""
list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
    index -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值。
"""

list1 = ['Google', 'Runoob', 'Taobao']

print('移除一个的元素 : ', list1.pop())
print(list1)
