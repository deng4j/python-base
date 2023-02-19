import os

"""
os.mkdir(path[, mode])：用于以数字权限模式创建单个目录。默认的模式为 0777 (八进制)。
    path -- 要创建的目录，可以是相对或者绝对路径。
    mode -- 要为目录设置的权限数字模式
"""

path = 'D:\\window\\temp\\test1\\test3'

os.mkdir(path, 0o777)
