"""
bytes.decode(encoding="utf-8", errors="strict")：
    encoding -- 要使用的编码，如"UTF-8"。
    errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore',
        'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
"""

str = "菊花残满地霜"

deStr = str.encode("UTF-8")
print(deStr)

deStr = deStr.decode("UTF-8", 'strict')
print(deStr)
