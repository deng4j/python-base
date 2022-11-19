import sys, importlib

"""
场景：倘若，更改了已经在 Python shell 中导入的模块，然后重新导入该模块，
    Python 会认为“我已经导入了该模块，不需要再次读取该文件”，所以更改将无效。

importlib.reload(module) 用于重新载入之前载入的模块。
"""

importlib.reload(sys)
