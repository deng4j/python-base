import os

"""
os.path.expanduser(path):把path中包含的"~"和"~user"转换成用户目录
"""

path = '~\\test.txt'

print(os.path.expanduser(path))

print(os.path.expanduser('~'))
print(os.path.expanduser('~user'))
