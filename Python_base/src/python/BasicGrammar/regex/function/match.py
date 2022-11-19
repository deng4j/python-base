import re

"""
re.match(pattern, string, flags=0)：尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。匹配成功re.match方法返回一个匹配的对象。
    pattern：正则表达式
    string：要匹配的字符串
    flags：
        re.I 忽略大小写
        re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
        re.M 多行模式
        re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
        re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
        re.X 为了增加可读性，忽略空格和 # 后面的注释
"""
print("--------------- match -----------------")

match1 = re.match('www', 'www.runoob.com')
print(match1)
print(match1.span())

match2 = re.match('com', 'www.runoob.com')
print(match2)

"""
使用group(num) 或 groups() 匹配对象函数来获取匹配表达式：
    group(num=0)：匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
    groups()：返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
    
group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
span([group]) 方法返回 (start(group), end(group))。
"""
print("--------------- group -----------------")

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.groups() : ", matchObj.groups())  # 等价于 (m.group(1), m.group(2), ...)
    print("matchObj.group() : ", matchObj.group())  # 获得整个匹配的子串
    print("matchObj.group(1) : ", matchObj.group(1))  # 返回第一个分组匹配成功的子串
    print("matchObj.group(2) : ", matchObj.group(2))  # 返回第二个分组匹配成功的子串
    print("matchObj.span(0) : ", matchObj.span(0))  # 返回匹配成功的整个子串的索引
    print("matchObj.span(1) : ", matchObj.span(1))  # 返回第一个分组匹配成功的子串的索引
else:
    print("No match!!")
