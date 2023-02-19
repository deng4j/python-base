"""
isdigit() 方法检测字符串是否只由数字组成。
"""

str1 = "123456"
print(str1.isdigit())

# 注意：str.isdigit中的str
digit_str = filter(str.isdigit, 'ab123cd')
print(list(digit_str))
