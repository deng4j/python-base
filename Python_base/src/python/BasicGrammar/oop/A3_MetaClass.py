"""
自定义元类控制类的创建：
    1.只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类。
"""


# 自定义元类
class Mymeta(type):
    def __init__(self, class_name, class_bases, class_dic):
        print('self:', self)
        print('class_name:', class_name)
        print('class_bases:', class_bases)
        print('class_dic:', class_dic)

        if not class_name.istitle():
            raise TypeError('类名首字母必须大写')
        super(Mymeta, self).__init__(class_name, class_bases, class_dic)  # 重用父类type的功能


# 使用自定义的元类
class people(object, metaclass=Mymeta):
    country = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("你好{}".format(self.name))


try:
    p = people("张三", 18)
except Exception as e:
    print(e)
