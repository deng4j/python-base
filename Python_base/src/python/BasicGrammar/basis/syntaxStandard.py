"""
Python没有三元表达式
行与缩进：缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。
"""

# 注释方式一

'''
多行注释二
'''

"""
多行注释三
"""

# TODO 编译工具识别，等待去做

print("-------------------------华丽分割线-------------------------")

# Python一行代表一句代码，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句

item_one = 1
item_two = 2
item_three = 3

total = item_one + \
        item_two + \
        item_three
print(total)

print("-------------------------华丽分割线-------------------------")

# Python 可以在同一行中使用多条语句，语句之间使用分号 ; 分割
str1 = "str1";
str2 = "str2"

print(str1)
print(str2)

print("-------------------------条件控制-------------------------")

a = 2
if a >= 1:
    print("a >= 1")
elif a <= 2:
    print("a <= 2")
else:
    print("?")

if -1:
    print("-1")

if 0:
    print("-1")

print('yes' if 2 > 1 else 'no')

print("-------------------------华丽分割线-------------------------")

a = []
b = [1]
if a:
    print(a)

if b:
    print(b)

print("--------------------------- del ----------------------------------")

# 删除引用
str3 = "aa"
del str3

try:
    print(str3)
except:
    print("NameError: name 'str3' is not defined")
