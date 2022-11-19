from io import StringIO

"""
StringIO在内存中读写str
"""

f = StringIO()
f.write('hello')
f.write(' world!')
print(f.getvalue())
