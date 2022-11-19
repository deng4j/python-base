"""
close()：用于关闭生成器。对关闭的生成器后再次调用next或send将抛出StopIteration异常。
"""


def repeater():
    n = 0
    while True:
        n = (yield n)


r = repeater()
print(next(r))

r.close()

try:
    print(next(r))
except StopIteration:
    print("StopIteration异常")
