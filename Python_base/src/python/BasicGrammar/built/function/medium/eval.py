"""
eval() 函数用来执行一个字符串表达式，并返回表达式的值。
"""

print("------------------------ 测试1 ------------------------------")

x = 7
print(eval('3 * x'))

n = 8
print(eval("n + 4"))

print("------------------------ 测试2 ------------------------------")


def foo():
    print("--- foo() ---")


eval('foo')()
