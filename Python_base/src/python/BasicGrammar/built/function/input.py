"""
input() 函数接受一个标准输入数据，返回为 string 类型。
"""

print(input("输入内容，按下enter 键后退出。\n"))

data = input(r"输入带\n的字符串：" + '\n')
print('\n结果：{}'.format(data))

print("--------------------多行输入----------------------")
for i in iter(input, '结束'):
    print(i)
