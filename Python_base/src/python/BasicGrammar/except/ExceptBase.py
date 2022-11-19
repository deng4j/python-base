print("----------------------- try-except -----------------------")
try:
    a = 1 / 0
except ZeroDivisionError:
    print("除0异常-division by zero")

print("----------------------- try-except(元组) -----------------------")

# 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组
try:
    a = 1 / 0
except (ZeroDivisionError, TypeError, NameError):
    print("除0异常-division by zero")

print("----------------------- try-except多异常捕获 -----------------------")
try:
    # a = 1 / 0
    b = int("bbb")
except ZeroDivisionError("除0异常-division by zero"):
    print("")
except ValueError:
    print("ValueError")

print("----------------------- try-except-else -----------------------")

try:
    a = 1 / 2
except ZeroDivisionError:
    print("除0异常-division by zero")
else:
    print("无异常时执行！")

print("----------------------- try-except-else-finally -----------------------")

try:
    a = 1 / 2
except ZeroDivisionError:
    print("除0异常-division by zero")
else:
    print("无异常时执行！")
finally:
    print("有无异常，最后我都要执行！")

print("----------------------- 抛异常raise  -----------------------")

try:
    a = 0
    if a == 0:
        raise ZeroDivisionError("除数为0 !!!!")
except ZeroDivisionError as e:
    print(e)
