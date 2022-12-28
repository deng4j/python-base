"""
super()：用于调用父类(超类)的一个方法。多继承情况下从左往右查找方法。
"""


class People:

    def __init__(self):
        print("People")

    def fight(self):
        print('人类打架')


class Animal:

    def __init__(self):
        print("Animal")

    def fight(self):
        print('动物打架')

    def growl(self):
        print('动物咆哮')


class Student(People, Animal):
    def __init__(self):
        super().__init__()  # 调用最左边父类People的构造方法
        super(People, self).__init__()  # 调用指定父类People右边Animal的构造方法
        Animal.__init__(self)  # Animal调用构造方法
        print("Student")


if __name__ == "__main__":
    student = Student()
    student.fight()
    student.growl()
