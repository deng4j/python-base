"""
hasattr：判断一个方法是否存在与这个类中
getattr：根据字符串去获取obj对象里的对应的方法的内存地址，加"()"括号即可执行
setattr：通过setattr将外部的一个函数绑定到实例中
delattr：删除一个实例或者类中的方法
"""


class People:
    country = 'China'

    def __init__(self, name):
        self.name = name

    def eat(self):
        print('%s is eating' % self.name)


p1 = People('nick')

print(hasattr(p1, 'eat'))

eatVar = getattr(p1, 'eat')
print(eatVar)
eatVar()

setattr(p1, 'country', "ASU")
print(p1.country)

delattr(p1, 'name')
try:
    print(p1.name)
except AttributeError as e:
    print(e)
