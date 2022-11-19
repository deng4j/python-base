print("------------------------ 递归函数 ------------------------")


def func12(i):
    print(i)
    i -= 1
    if i <= 0:
        return
    func12(i)


func12(10)
