"""
非绑定方法:在类内部使用 @staticmethod 修饰的方法即为非绑定方法，这类方法和普通定义的函数没有区别，
不与类或对象绑定，谁都可以调用，且没有自动传值的效果。
"""


class Person:
    country = "China"

    @staticmethod
    def info():
        print("@staticmethod  info()")


Person.info()
