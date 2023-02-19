import os

"""
os.openpty()：用于打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
"""

# 主 pty, 从 tty
m, s = os.openpty()

print(m)
print(s)

# 显示终端名
s = os.ttyname(s)
print(m)
print(s)
