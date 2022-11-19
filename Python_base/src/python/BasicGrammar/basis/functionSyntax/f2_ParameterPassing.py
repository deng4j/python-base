"""
不可更改(immutable)对象(值传递)：strings, tuples, 和 numbers ，作为参数，传递的是该参数值相同的新克隆对象
可更改(mutable)对象(引用传递)：list,dict，作为参数，传递的是该引用
"""

print("---------------------- 值传递 ----------------------")


def func5(parma):
    parma += 5
    print("参数parma的id：", id(parma))


a = 10
func5(a)
print("数字a的值：%d，数字a的id：%d" % (a, id(a)))

print("---------------------- 引用传递 ----------------------")


def func6(list):
    list.append(5)


b = [1, 2, 3, 4]
func6(b)
print(b)
