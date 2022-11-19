"""
元类:
    1.如果说类也是对象，那么用class关键字的去创建类的过程也是一个实例化的过程，该实例化的目的是为了得到一个类，调用的是元类。
    2.用class关键字创建一个类，用的默认的元类type，因此以前说不要用type作为类别判断。
"""

class_name = 'People'  # 类名

class_bases = (object,)  # 基类

class_dic = {}  # 类的名称空间

class_body = """
country = "China"

def __init__(self, name, age):
    self.name = name
    self.age = age
    
def say(self):
    print("你好{}".format(self.name))
"""

# 执行class_body，将名字丢入class_dic
exec(class_body, {}, class_dic, )
print(class_dic)

New_People = type(class_name, class_bases, class_dic)
print(New_People)

people = New_People("张三", 18)
print(people.name)
people.say()

"""
实例化步骤:
    1.拿到类名：class_name = 'Person'
    2.拿到类的基类：class_bases = (Object,)
    3.执行类体代码，拿到类的命名空间：class_dic = {...}
    4.调用元类得到类：Person = type(class_name,class_bases,class_dic)
"""
