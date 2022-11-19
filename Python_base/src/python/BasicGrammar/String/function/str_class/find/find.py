"""
str.find(str, beg=0, end=len(str_class))：从左开始查找第一个子字符串，如果指定开始和结束范围，则在范围内检测，
    如果存在着返回索引值，否则返回-1。

    str -- 指定检索的字符串
    beg -- 开始索引，默认为0。
    end -- 结束索引，默认为字符串的长度。
"""

str1 = "等一等baby，这些伤会自由baby"
str2 = "baby"

print(str1.find(str2))
print(str1.find(str2, 5))  # 从索引5开始查找
print(str1.find(str2, 0, 6))  # 从0 - 6中查找
