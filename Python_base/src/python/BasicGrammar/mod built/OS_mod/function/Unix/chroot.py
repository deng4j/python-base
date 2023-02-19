import os

"""
os.chroot(path)：用于更改当前进程的根目录为指定的目录，使用该函数需要管理员权限。在 unix 中有效。
"""

path = "D:\\window\\temp\\test.txt"

# 设置根目录
os.chroot(path)
