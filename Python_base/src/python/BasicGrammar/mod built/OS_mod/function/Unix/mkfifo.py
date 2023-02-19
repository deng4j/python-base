import os

"""
os.mkfifo(path[, mode])：用于创建指令路径的管道，并设置权限模式。默认的模式为 0666 (八进制)。
    path -- 要创建的目录，可以是相对或者绝对路径。
    mode -- 要为目录设置的权限数字模式
"""

path = 'D:\\window\\temp\\test1\\test4'

os.mkfifo(path, 0o777)
