"""
list.sort( key=None, reverse=False) 用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
    key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
    reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
"""

print("-------------------------默认排序------------------------------")

aList = ['Google', 'Runoob', 'Taobao', 'Facebook']

aList.sort()
print("List : ", aList)

print("-----------------------指定排序--------------------------------")


# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]


# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# 指定第二个元素排序
random.sort(key=takeSecond)

print('排序列表：', random)
