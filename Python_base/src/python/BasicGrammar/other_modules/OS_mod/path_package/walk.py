import os

"""
os.path.walk(path, visit, arg)：遍历path，进入每个目录都调用visit函数，
    visit函数必须有3个参数(arg, dirname, names)，
        dirname表示当前目录的目录名，
        names代表当前目录下的所有文件名，
        args则为walk的第三个参数
"""

path1 = 'D:\\window\\temp\\'


# 回调函数
def find_file(arg, dirname, files):
    for file in files:
        file_path = os.path.join(dirname, file)
        if os.path.isfile(file_path):
            print("find file:%s" % file_path)


os.path.walk(path1, find_file, ())
