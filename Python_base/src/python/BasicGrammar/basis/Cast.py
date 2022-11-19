#
"""
Python3 数据类型转换:
    对数据内置的类型进行转换，数据类型的转换，一般情况下你只需要将数据类型作为函数名即可。
    隐式类型转换 - 自动完成
    显式类型转换 - 需要使用类型函数来转换
"""

print("------ 整型数据与浮点类型的数据进行相加 ------")

num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:", type(num_int))
print("datatype of num_flo:", type(num_flo))

print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))

print("------ 整型数据与字符串类型的数据进行相加 ------")

num_int = 123
num_str = "456"

print("Data type of num_int:", type(num_int))
print("Data type of num_str:", type(num_str))

print(str(num_int) + num_str)
