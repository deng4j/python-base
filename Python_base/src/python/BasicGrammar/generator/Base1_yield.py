from collections.abc import Iterable

"""
使⽤了yield关键字的函数不再是函数，⽽是⽣成器。（使⽤了yield的函数就是⽣成器）

生成器是一个返回迭代器的函数，生成器的本质就是迭代器，同时也并不仅仅是迭代器，生成器提供了非常方便的自定义迭代器的途径
在函数中但凡出现yield关键字，再调用函数，就不会继续执行函数体代码，而是会返回一个值。

yield关键字有两点作⽤：
    1.保存当前运⾏状态（断点），然后暂停执⾏，即将⽣成器（函数）挂起
    2.将yield关键字后⾯表达式的值作为返回值返回，此时可以理解为起到了return的作⽤
"""

print("---------------------1-----------------------")


def func():
    print(1)
    yield
    print(2)
    yield


g = func()
print(g)

print("-------------------2-------------------------")


def func():
    print('from func 1')
    yield 'a'
    print('from func 2')
    yield 'b'


g = func()
print(F"g.__iter__() == g: {g.__iter__() == g}")

res1 = g.__next__()
print(f"res1: {res1}")

res2 = next(g)
print(f"res2: {res2}")

print("-------------------3-------------------------")


def func():
    print('from func 1')
    yield 'a'
    print('from func 2')
    yield 'b'


g = func()
for i in g:
    print(i)

print(f"list(func()): {list(func())}")

print(isinstance(g, Iterable))
