"""
memoryview(obj)：返回给定参数的内存查看对象(memory view)。

所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许Python代码访问。
"""

m = memoryview(b"abcd")
print(m)
print(m[1])
