"""
多继承class DerivedClassName(Base1, Base2, Base3)：
    1.需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，
    2.python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
"""


class People:
    name = None

    # 构造方法
    def __init__(self, **vardict):
        self.name = vardict.get("name")
        if self.name is None:
            self.name = "人类"

    # 自定义方法
    def getName(self):
        return self.name


class Animal:
    name = None

    # 构造方法
    def __init__(self):
        print("Animal.class")
        self.name = "动物"

    # 自定义方法
    def getName(self):
        return self.name


class Student(People, Animal):

    # 重写方法
    def getName(self):
        return self.name


print("------------------- 继承 -------------------")

stu1 = Student()
stu2 = Student(name="南华大学-张三")  # 未重写父类的构造方法
print(stu1.getName())
print(stu2.getName())
