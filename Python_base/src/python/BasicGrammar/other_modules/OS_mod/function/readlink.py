import os

"""
os.readlink(path)：用于返回软链接所指向的文件，可能返回绝对或相对路径。

os.symlink()以管理员身份运行pycharm
"""

src = 'D:\\window\\temp\\test.txt'
dst = 'D:\\window\\temp\\test\\testPopen\\test.txt'

# 创建软链接
os.symlink(src, dst)

# 使用软链接显示源链接
path = os.readlink(dst)
print(path)
