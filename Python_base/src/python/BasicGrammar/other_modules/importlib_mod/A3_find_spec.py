import importlib.util

"""
importlib.util.find_spec(module_name) 检查并观察一个模块是否可以引入,而不是仅仅是猜测，没有找到返回None，否则返回该模块的说明。
importlib.util.module_from_spec(module_spec) 它接受由check_module函数返回的模块说明，返回引入的模块。
"""

import importlib.util
import importlib


def check_module(module_name):
    module_spec = importlib.util.find_spec(module_name)
    if module_spec is None:
        print("Module :{} not found".format(module_name))
        return None
    else:
        print("Module:{} can be imported!".format(module_name))
        return module_spec


def import_module_from_spec(module_spec):
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    module_spec = check_module("mod")
    if (module_spec):
        module = import_module_from_spec(module_spec)
        print(dir(module))
