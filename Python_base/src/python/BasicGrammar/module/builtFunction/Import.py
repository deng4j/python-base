"""
__import__(name[, globals[, locals[, fromlist[, level]]]])：用于动态加载类和函数。
"""

M = __import__("mod")  # 动态导入模块

M.printA()
