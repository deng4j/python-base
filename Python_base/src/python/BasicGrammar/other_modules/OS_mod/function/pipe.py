import os

"""
os.pipe() 方法用于创建一个管道, 返回一对文件描述符(r, w) 分别为读和写。
"""

# 文件描述符 r, w 用于读、写
r, w = os.pipe()

print(r, w)
