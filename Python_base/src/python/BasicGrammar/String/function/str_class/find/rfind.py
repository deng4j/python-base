"""
str.rfind(str, beg=0 end=len(str_class))：查找指定字符串最后一次出现的位置，没有则返回-1。
    str -- 查找的字符串
    beg -- 开始查找的位置，默认为0
    end -- 结束查找位置，默认为字符串的长度。
"""

str1 = 'ABCD你妹的，就这？'

print(str1.rfind('妹'))
print(str1.rfind('妹', 0, 4))
