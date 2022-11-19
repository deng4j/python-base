"""
compile(source, filename, mode[, flags[, dont_inherit]])：将一个字符串编译为字节代码。
    source -- 字符串或者AST（Abstract Syntax Trees）对象。。
    filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
    mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
    flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。。
    flags和dont_inherit是用来控制编译源码时的标志
"""

str = "for i in range(0,10): print(i)"

c = compile(str, '', 'exec')

exec(c)
