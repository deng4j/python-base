import os

path = 'D:\\window\\temp\\test.txt'

print(os.path.getatime(path))  # 输出最近访问时间
print(os.path.getctime(path))  # 输出文件创建时间
print(os.path.getmtime(path))  # 输出最近修改时间
print(os.path.getsize(path))  # 输出文件大小（字节为单位）

