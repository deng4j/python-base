import os

"""
os.symlink(src, dst)：用于创建一个软链接。os.symlink()以管理员身份运行pycharm。
    src -- 源地址。
    dst -- 目标地址。
"""

src = 'D:\\window\\temp\\test.txt'
dst = 'D:\\window\\temp\\test\\testPopen\\test.txt'

# 创建软链接
os.symlink(src, dst)
