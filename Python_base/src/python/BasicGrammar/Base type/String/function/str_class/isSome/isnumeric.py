"""
isnumeric() 方法检测字符串是否只由数字组成，数字可以是： Unicode 数字，全角数字（双字节），罗马数字，汉字数字。
指数类似 ² 与分数类似 ½ 也属于数字。
"""

str1 = "12346   "
str2 = "12346"

print(str1.isnumeric())
print(str2.isnumeric())

print("---------------------- Unicode 数字 --------------------------")

s = '\u00B23455'  # ²3455
print(s.isnumeric())

s = '\u00BD'  # ½
print(s.isnumeric())
