"""
创建Bytes：
    1.字符串的内容都是 ASCII 字符，那么直接在字符串前面添加b前缀就可以转换成 bytes。
    2.bytes 是一个类，调用它的构造方法，也就是 bytes()，可以将字符串按照指定的字符集转换成 bytes；如果不指定字符集，那么默认采用 UTF-8。
    3.字符串本身有一个 encode() 方法，该方法专门用来将字符串按照指定的字符集转换成对应的字节串；如果不指定字符集，那么默认采用 UTF-8。
"""

# 通过构造函数创建空 bytes
b1 = bytes()
# 通过空字符串创建空 bytes
b2 = b''

# 通过b前缀将字符串转换成 bytes
b3 = b'https'
print("b3: ", b3)
print(b3[3])
print(b3[7:22])

# 为 bytes() 方法指定字符集
b4 = bytes('你妹妹', encoding='UTF-8')
print("b4: ", b4)

# 通过 encode() 方法将字符串转换成 bytes
b5 = "你妹妹".encode('UTF-8')
print("b5: ", b5)

# 通过 decode() 方法将 bytes 转换成字符串
str1 = b5.decode('UTF-8')
print("str1: ", str1)

# 通过 str() 方法将 bytes 转换成字符串
print(str(b5, 'UTF-8'))

# 数字转byte
b1 = bytes([24])
print(b1)

# byte转数字
print(int.from_bytes(b1, 'big'))

# 拼接
b1 = b'a' + b'bcde'
print(b1)

python = (b'P' b'y' b"t" b'o' b'n')
print(python)
