str1 = '人生苦短，我用Python!'
bytearray1 = bytearray(str1.encode())
print(bytearray1)

# bytearray里的值是可以修改的
print(bytearray1[0:1])

# 解码
deStr = bytearray1.decode()
print(deStr)
