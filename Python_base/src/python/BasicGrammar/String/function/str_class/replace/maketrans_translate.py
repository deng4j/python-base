"""
str_class.maketrans(x[, y[, z]])：用于创建字符映射的转换表，替换字符串。
    x -- 必需，字符串中要替代的字符组成的字符串。
    y -- 可选，相应的映射字符的字符串。
    z -- 可选，要删除的字符。
"""

"""
translate() 方法根据参数 table 给出的表(包含 256 个字符)转换字符串的字符,要过滤掉的字符放到 deletechars 参数中。

str.translate(table)
bytes.translate(table[, delete])
bytearray.translate(table[, delete])
    table -- 翻译表，翻译表是通过 maketrans() 方法转换而来。
    deletechars -- 字符串中要过滤的字符列表。
"""

print("--------------------------------------")

str1 = "你妹的!"
mytable = str1.maketrans("妹", "*")

newStr1 = str1.translate(mytable)
print(newStr1)

print("--------------------------------------")

str2 = '哈哈哈哈哈霍霍霍霍叽叽歪歪你妹的！'

x = '妹'
y = '*'
z = '哈叽'

mytable = str2.maketrans(x, y, z)
newStr2 = str2.translate(mytable)
print(newStr2)

print("--------------------------------------")

bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# 转换为大写，并删除字母o
print(b'runoob'.translate(bytes_tabtrans, b'o'))
