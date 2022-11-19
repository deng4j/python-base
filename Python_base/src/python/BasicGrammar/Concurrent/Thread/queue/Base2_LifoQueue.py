import queue

"""
线程队列：与队列用法一致

queue.LifoQueue(maxsize=0)：后进先出
"""

q = queue.LifoQueue()
q.put('first')
q.put('second')
q.put('third')

print(q.get())
print(q.get())
print(q.get())
