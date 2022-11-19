import os

"""
os.chdir(path)：用于改变当前工作目录到指定的路径。允许访问返回 True , 否则返回False。
"""

retval = os.getcwd()
print("当前工作目录为：", retval)

# 修改当前工作目录
os.chdir("D:\\window\\temp")

print("当前工作目录为：", os.getcwd())
