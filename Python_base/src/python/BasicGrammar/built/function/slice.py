"""
class slice(start, stop[, step])：实现切片对象，主要用在切片操作函数里的参数传递。
    start -- 起始位置
    stop -- 结束位置
    step -- 间距
"""

myslice1 = slice(5)  # 设置截取5个元素的切片
myslice2 = slice(1, 8, 2)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(arr[myslice1])
print(arr[myslice2])
