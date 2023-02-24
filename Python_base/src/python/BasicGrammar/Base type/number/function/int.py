"""
int.from_bytes(bytes, byteorder, *, signed=False):byte转整数
    bytes：要转换的十六进制，如\xf1\xff
    byteorder：选'big'和'little'，其中big代表正常顺序，即f1ff。little反之，代表反序fff1；
    signed：选True、Flase表示是否要区分二进制的正负数含义。即是否要对原二进制数进行原码反码 补码操作。

int.to_bytes(length, byteorder, *, signed=False):整数转byte
"""

print("----------------- 转化 -----------------")

print(int(-12.94))  # 浮点转int
print(int('+1008'))  # 字符串转int
print(int('-008'))

# 转换为一个十进制整数
a1 = int("1", 10)
print(a1)

a2 = int(0xFF)
print(a2)

print("----------------- 二进制 -----------------")

s1 = b'\xf1\xff'
print(int.from_bytes(s1, byteorder='little', signed=True))

print(int(-15).to_bytes(2, byteorder='little', signed=True))
