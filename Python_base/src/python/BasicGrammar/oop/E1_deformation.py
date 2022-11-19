"""
类中所有双下划线开头的名称如__x都会自动变形成：_类名__x的形式：
    1.在继承中，父类如果不想让子类覆盖自己的方法，可以将子类方法定义为私有的。

自动变形的特点：
    1.类中定义的__x只能在内部使用，如self.__x，引用的就是变形的结果。
    2.这种变形其实正是针对内部的变形，在外部是无法通过__x这个名字访问到的。
    3.在子类定义的__x不会覆盖在父类定义的__x，因为子类中变形成了：_子类名__x,而父类中变形成了：_父类名__x，即双下滑线开头的属性在继承给子类时，子类是无法覆盖的。
"""


class People:
    __N = 0

    def __fo(self):  # 在这边操作
        print("People  __fo")

    def test(self):
        self.__fo()
        self._People__fo()  # 方法变形
        print("----------- -----------")
        self._Student__fo()


class Student(People):

    def __init__(self) -> None:
        self._Student__N = 10

    def __fo(self):
        print("Student  __fo")


print("------------------- 测试覆盖 -------------------")

stu1 = Student()
stu1.test()

print("-----------------------")

print(stu1._People__N)  # 属性变形
print(stu1._Student__N)
print(Student._People__N)
print(People._People__N)

print("-----------------------")

stu1._Student__N = 20
print(stu1._Student__N)
