"""
属性告诉您在任何具有__dict__对象的实例对象中找到指向该对象的指针的位置的偏移量。它以字节为单位。
"""

class Aoo:
    a = None
    b = 13
    c = 'a'
    d = 14


print(Aoo.__dictoffset__)
Aoo.__flags__