"""
pow(x, y[, z])：计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z

内置pow()函数则会把参数转换为 int
"""

print("2^3 % 3 : ", pow(2, 3, 3))
