import time

now_time = time.localtime()  # 结构化时间

print("----------------------------- 把结构化时间转换为时间戳格式 --------------------------------\n")

print(time.mktime(now_time))

print("----------------------------- 把结构化时间转换为格式化时间 --------------------------------\n")

# %Y年-%m月-%d天 %X时分秒=%H时:%M分:%S秒
print(time.strftime("%Y-%m-%d %X", now_time))

# asctime()默认参数为time.localtime()，形式'Sun Jun 20 23:21:05 1993'
print(time.asctime())

print("----------------------------- 时间戳转化为time.asctime()的形式 --------------------------------\n")

# time.ctime()默认参数是time.time()
print(time.ctime())
print(time.ctime(time.time()))

print("----------------------------- 把格式化时间化为结构化时间 --------------------------------\n")

print(time.strptime('2022-05-20 13:14:52', '%Y-%m-%d %X'))
