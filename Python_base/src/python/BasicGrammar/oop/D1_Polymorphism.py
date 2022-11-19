"""
Python说多态似乎没有意义
"""


class People:
    name = None

    # 构造方法
    def __init__(self):
        self.name = "人类"

    # 自定义方法
    def getName(self):
        return self.name


class Student:
    name = "学生"

    # 重写方法
    def getName(self):
        return self.name


print("------------------- 伪多态 -------------------")


def getName(obj_people):
    print(obj_people.getName())


p = People()
stu = Student()

getName(p)
getName(stu)
