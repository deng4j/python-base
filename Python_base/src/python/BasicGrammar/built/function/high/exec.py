"""
exec(object[, globals[, locals]])： 执行储存在字符串或文件中的 Python 语句
    object：必选参数，表示需要被指定的 Python 代码。它必须是字符串或 code 对象。如果 object 是一个字符串，
        该字符串会先被解析为一组 Python 语句，然后再执行（除非发生语法错误）。如果 object 是一个 code 对象，
        那么它只是被简单的执行。
    globals：可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象。
    locals：可选参数，表示当前局部命名空间（存放局部变量），如果被提供，可以是任何映射对象。
        如果该参数被忽略，那么它将会取与 globals 相同的值。
"""

code = """
x=1
print('exec函数运行了')
def func(self):
    pass
"""
class_dic = {}
# 执行cmd中的代码，然后把产生的名字丢入class_dic字典中
exec(code, {}, class_dic)

print(class_dic)

print("-------------------------------------------------------")

code = """

class Person:
    country = "China"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("你好{}".format(self.name))

"""
class_dic = {}
exec(code, {}, class_dic)
print(class_dic)
