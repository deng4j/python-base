print("------------------ return -------------------")

"""
⽣成器客户以使⽤return 关键字，语法上没有问题，但是如果执⾏到 return 语句以后，⽣成器会停⽌ 迭代，抛出停⽌迭代的异常。
"""


def i_wanna_return():
    yield 'a'
    print('插播一条广告🪧')
    yield 'b'
    return None
    yield 'c'


for i in i_wanna_return():
    print(i)

print("------------------ 迭代器套迭代器 -------------------")


def sub_generator():
    yield 1
    yield 2
    for i in range(3):
        yield i


for i in sub_generator():
    print(i)

print("------------------ 迭代器套迭代器 -------------------")


def sub_generator():
    yield 1
    yield 2
    yield from range(3)


for i in sub_generator():
    print(i)
