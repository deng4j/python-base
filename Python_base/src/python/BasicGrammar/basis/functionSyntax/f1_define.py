"""
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号 : 起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。
"""

print("--------------- 函数1 ----------------")


def func1(): {
    print("func1()")
}


def func2(): var = {
    print("func2")
}


def func():
    print("func()")


func1()
func2()
func()

print("--------------- 函数2 ----------------")


def func4(a, b):
    if a > b:
        return "a"
    else:
        return "b"


print(func4(1, 2))
print(func4(b=2, a=1))

print("--------------- 函数3 ----------------")


def func(s='sssss'):
    print(s)


func()
