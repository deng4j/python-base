from concurrent.futures import ProcessPoolExecutor
import os, time


def task(taskName):
    strName = "任务：" + str(taskName)
    print(strName)
    time.sleep(0.2)
    return str(os.getpid()) + ":" + str(taskName)


if __name__ == '__main__':
    executor = ProcessPoolExecutor(max_workers=3)

    # map取代了for+submit
    executor.map(task, range(1, 10))
