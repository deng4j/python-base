"""
面向对象:
    类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    方法：类中定义的函数。
    类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
    数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
    方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
    局部变量：定义在方法中的变量，只作用于当前实例的类。
    实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
    继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。
    实例化：创建一个类的实例，类的具体对象。
    对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

Python不需要重载，因为重载是解决不同参数的问题的

类属性与方法:
    1.Python默认情况下，所有成员都是公共的
    2.__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。
    3.__private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。
    在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。
        self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定使用 self。
    4.内置变量：双下划线开头且结尾的变量，在 Python 中被称为内置变量，如__name__，在本模块是__main__，在导入的模块中是该模块的缩写

类的专有方法：
    __init__ : 构造函数，在生成对象时调用
    __del__ : 析构函数，释放对象时使用
    __repr__ : 打印，转换
    __setitem__ : 按照索引赋值
    __getitem__: 按照索引获取值
    __len__: 获得长度
    __cmp__: 比较运算
    __call__: 函数调用
    __add__: 加运算
    __sub__: 减运算
    __mul__: 乘运算
    __truediv__: 除运算
    __mod__: 求余运算
    __pow__: 乘方
    __str__: 打印对象时调用
"""

print("------------------- People -------------------")


# 自定义一个People class
class People:
    name = None  # 定义属性方式1
    __leg = '腿'

    # 构造方法
    def __init__(self, **vardict):
        self.age = 18  # 定义属性方式2
        self.name = vardict.get("name")
        if self.name is None:
            self.name = "人类"

    def __getYou(self):
        print('__getYou')

    # 自定义方法
    def getName(self):
        print(self.__leg)
        self.__getYou()
        return self.name


# 实例化类
p1 = People()
p2 = People(name="李四")

# 定义属性方式3，属于该class
People.number1 = 2000
print(p1.number1)
print(p2.number1)

# 定义属性方式4，属于该实例
p2.number2 = 3000
try:
    print(p1.number2)
except AttributeError as e:
    print(e)
print(p2.number2)

print("------------------------------------------------")

print(p1.getName())
print(p1.name)
print(p1.age)
print(p2.getName())
