import math

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
