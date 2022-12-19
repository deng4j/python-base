"""
next(iterable[, default])：返回迭代器的下一个项目。要和生成迭代器的 iter() 函数一起使用。
"""

list = [1, 2, 3, 4]

it = iter(list)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素
print(next(it))  # 输出迭代器的下一个元素

print("--------------- 迭代器对象 ---------------")

for x in it:
    print(x, end=" ")
print()

print("--------------- 创建迭代器对象 ---------------")


# 创建一个迭代器，把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__()
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))

print("--------------- 字符串迭代 ---------------")

i = iter('abcd')
print(next(i))

print("--------------- 迭代中止 ---------------")

it = iter(input, '3')  # 遇到'3'中止

try:
    while it:
        print(next(it))
except:
    pass
