def func1(x):
    print("func1() - x：", x)
    y = 5

    def func2(x):
        x += 1
        print("func2() - x：", x)
        print("func2() - y：", y)

    func2(8)


func1(10)
