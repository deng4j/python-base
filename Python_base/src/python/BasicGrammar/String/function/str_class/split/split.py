"""
str.split(str="", num=str_class.count(str))：通过指定分隔符对字符串进行切片，如果第二个参数 num 有指定值，则分割为 num+1 个子字符串。
    str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
    num -- 分割次数。默认为 -1, 即分隔所有。
"""

str1 = 'aaa bbb ccc ddd'

list1 = str1.split(' ')
print(list1)
print(type(list1))

list2 = str1.split(' ', 1)
print(list2)
