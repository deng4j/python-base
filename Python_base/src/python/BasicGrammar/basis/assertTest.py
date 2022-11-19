"""
assert用于判断一个表达式，在表达式条件为 false 的时候触发异常。断言可以在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况。
"""

assert True

assert 1 == 1

try:
    assert 1 == 2
except:
    print('捕捉到错误')

assert 1 == 2, '1 不等于 2'  # 跟参数
