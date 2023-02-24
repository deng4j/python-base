import os

"""
os.makedirs(name, mode=511, exist_ok=False)：用于递归创建多层目录。如果子目录创建失败或者已经存在，会抛出一个 OSError 的异常。
    path -- 需要递归创建的目录，可以是相对或者绝对路径。
    mode -- 权限模式，默认的模式为 511 (八进制)。。
    exist_ok：是否在目录存在时触发异常。如果 exist_ok 为 False（默认值），则在目标目录已存在的情况下触发 FileExistsError 异常；
        如果 exist_ok 为 True，则在目标目录已存在的情况下不会触发 FileExistsError 异常。
"""

path = 'D:\\window\\temp\\test1\\test2'

os.makedirs(path, 0o777)
