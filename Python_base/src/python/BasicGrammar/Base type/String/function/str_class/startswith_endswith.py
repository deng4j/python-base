"""
str.endswith(suffix[, start[, end]])：判断字符串是否以指定后缀结尾。
    "suffix -- 该参数可以是一个字符串或者是一个元素。
    start -- 字符串中的开始位置。
    end -- 字符中结束位置。

str.endswith(prefix[, start[, end]])：与endwith()一样
"""

str = '你妈妈是我的baby'
suffix = 'baby'

print("--------------------------- endswith() -------------------------------")

print(str.endswith(suffix))
print(str.endswith(suffix, 5))
print(str.endswith(suffix, 0, 6))

print("--------------------------- endswith() -------------------------------")

prefix = "你妈"

print(str.startswith(prefix))
print(str.startswith(prefix, 5))
print(str.startswith(prefix, 0, 6))
