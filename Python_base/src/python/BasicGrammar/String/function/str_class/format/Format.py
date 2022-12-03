import math

"""
%s    字符串 (采用str()的显示)
%r    字符串 (采用repr()的显示)
%c    单个字符
%b    二进制整数
%d    十进制整数
%i    十进制整数
%o    八进制整数
%x    十六进制整数
%e    指数 (基底写为e)
%E    指数 (基底写为E)
%f    浮点数
%F    浮点数，与上相同
%g    指数(e)或浮点数 (根据显示长度)
%G    指数(E)或浮点数 (根据显示长度)
%%    字符"%"
"""

print("--------------------- format() ---------------------")

print('{:.2f}'.format(12.213232242))

print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))

print('{0} 和 {1}'.format('Google', 'Runoob'))

print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))

print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))

print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

# 传入一个字典, 然后使用方括号 [] 来访问键值
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))

# 在 table 变量前使用 ** 来访问键值
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))

print("--------------------- % ---------------------")

print("我叫 %s 今年 %d 岁!" % ('小明', 10))

print("--------------------- f-str_class ---------------------")
"""
f-str_class 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去
替换了 % 方式，不用再去判断使用 %s，还是 %d
"""
name = 'Runoob'

print("f-str_class：", 'Hello %s' % name)
print("f'：", f'Hello {name}')
print("f'：", f'{1 + 10}')
