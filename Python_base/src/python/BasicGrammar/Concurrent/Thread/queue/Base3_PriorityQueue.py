import queue

"""
线程队列：与队列用法一致

queue.PriorityQueue(maxsize=0)：存储数据时可设置优先级的队列
"""

q = queue.PriorityQueue()
# put进入一个元组,元组的第一个元素是优先级(通常是数字,也可以是非数字之间的比较),数字越小优先级越高
q.put((20, 'a'))
q.put((10, 'b'))
q.put((30, 'c'))

print(q.get())
print(q.get())
print(q.get())
