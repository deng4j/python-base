import os

"""
os.path.normcase(path):将指定路径中的所有字符都转换为小写，并将正斜杠('/')转换为反斜杠('\')。
"""

path = 'D:\\window\\temp\\test.txt'

print(os.path.normcase(path))
print(os.path.normcase('c:/a/b'))

