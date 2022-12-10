"""
convertScaleAbs(src[, dst[, alpha[, beta]]]) -> dst
    [, a[, b]]：嵌套形式表示 b 是独立于 a 的可选参数，即在传入 a 的情况下，b 可以自由地选择传入或省略。
    [, a, b] ：扁平形式表示 a 与 b 合在一起是一组可选参数，即 a 和 b 必须同时传入或者同时省略，但不能只传入一个

总之，你只能自由地拿掉或者保留一整个方括号中的内容，而不能将其拆开。

若要在某个层中两个或两个以上参数的其中某些参数可选，可以使用 = 赋给其默认值。
"""

def fun(p1=0, p2=None):
    """
    :param p1: default 0
    :param p2: default None
    :return: (p1, p2)
    """
    return p1, p2


print(fun())
