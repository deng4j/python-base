"""
with 的
with 语句适用于对资源进行访问的场合，作用等效于 try/finally，确保不管使用过程中是否发生异常
都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭／线程中锁的自动获取和释放等。
"""

with open('./test_runoob.txt', 'r') as f:
    read_data = f.read()
