from concurrent.futures import ProcessPoolExecutor


def work(code):
    if str(code).__eq__("200"):
        return "200"


def getCode(future):
    result_ = "获取成功：" + str(future.result())
    print(result_)


if __name__ == '__main__':
    p = ProcessPoolExecutor(3)

    codes = [404, 500, 200, 303]

    for code in codes:
        p.submit(work, code).add_done_callback(getCode)
