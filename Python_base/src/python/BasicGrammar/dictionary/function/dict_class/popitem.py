"""
popitem() 方法随机返回并删除字典中的最后一对键和值。空字典调用会抛异常。
"""

site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}

result = site.popitem()

print('返回值 = ', result)
print('site = ', site)
