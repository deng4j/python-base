"""
for item in Iterable 循环的本质就是先通过iter()函数获取可迭代对象Iterable的迭代器，然后对获取到的
迭代器不断调⽤next()⽅法来获取下⼀个值并将其赋值给item，当遇到StopIteration的异常后循环结 束。
"""
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    if x == "C++":
        continue
    if x == "Perl":
        break
    print(x)
else:
    print("正常退出循环!")

print("---------------------------------------------")

for i in range(0, 10):
    print(i, end=' ')
else:
    print("正常退出循环!")

print("---------------------------------------------")

for i in 'abcdefg':
    print(i)
