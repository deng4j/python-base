import importlib

"""
importlib.import_module(module_name) 导入模块
"""


def dynamic_import(module):
    return importlib.import_module(module)


if __name__ == "__main__":
    module = dynamic_import('mod')
    module.func()
