"""
函数的返回值如果有多个，以元组方式返回。
"""


def getResult1():
    return 1, 2, 3


def getResult2():
    return 1, [2, 3]


result1 = getResult1()
result2 = getResult2()

print(result1)
print(result2)
