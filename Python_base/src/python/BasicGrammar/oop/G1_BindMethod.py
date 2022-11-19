"""
 对象的绑定方法：在类中没有被任何装饰器修饰的方法就是 绑定到对象的方法，这类方法专门为对象定制。
    1.speak即为绑定到对象的方法，这个方法不在对象的名称空间中，而是在类的名称空间中。
    2.类中使用 @classmethod 修饰的方法就是绑定到类的方法。这类方法专门为类定制。
    通过类名调用绑定到类的方法时，会将类本身当做参数传给类方法的第一个参数。
    约定俗成第一个参数名为cls，也可以定义为其他参数名。


通过对象调用绑定到对象的方法，会有一个自动传值的过程，即自动将当前对象传递给方法的
第一个参数（self，一般都叫self，也可以写成别的名称）；若是使用类调用，则第一个参数需要手动传值。
"""


class Person:
    country = "China"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(self.name + ', ' + str(self.age))

    @classmethod
    def info(cls):
        print(cls.country)


print("------------------------ 绑定方法 ---------------------------")

p = Person('Kitty', 18)
print(p.__dict__)
print(Person.__dict__['speak'])

print("------------------------ 调用 ---------------------------")

p.speak()  # 通过对象调用
Person.speak(p)  # 通过类调用

print("------------------------ @classmethod ---------------------------")

p.info()
Person.info()
