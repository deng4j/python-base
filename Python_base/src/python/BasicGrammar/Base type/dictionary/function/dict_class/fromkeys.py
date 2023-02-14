"""
dict.fromkeys(seq[, value])：用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
    seq -- 字典键值列表。
    value -- 可选参数, 设置键序列（seq）对应的值，默认为 None。
"""

seq = ('name', 'age', 'sex')

tinydict = dict.fromkeys(seq)
print("新的字典为 : {}".format(str(tinydict)))

tinydict = dict.fromkeys(seq, 10)
print("新的字典为 : {}".format(str(tinydict)))
