from multiprocessing import Process, Queue


def task(q, i):
    q.put(i)


if __name__ == "__main__":
    queue = Queue()
    lists = []
    for i in range(1, 10):
        p = Process(target=task, args=(queue, i,))
        p.start()
        lists.append(p)

    for p in lists:
        p.join()

    for i in range(0, queue.qsize()):
        print(queue.get())
