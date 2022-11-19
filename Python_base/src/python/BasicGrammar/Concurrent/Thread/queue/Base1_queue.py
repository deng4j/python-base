import queue

"""
线程队列：与队列用法一致

queue.Queue(maxsize=0)：先进先出
"""

q = queue.Queue()
q.put('first')
q.put('second')
q.put('third')

print(q.get())
print(q.get())
print(q.get())
