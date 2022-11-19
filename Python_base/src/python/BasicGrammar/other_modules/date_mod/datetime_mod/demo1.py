import datetime
import time

print(datetime.datetime.now())  # 返回当前时间

print(datetime.date.fromtimestamp(time.time()))

# 当前时间+3天
timedelta = datetime.timedelta(3)
print(timedelta)
print(datetime.datetime.now() + timedelta)

# 当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(-3))

# 当前时间+30分钟
print(datetime.datetime.now() + datetime.timedelta(minutes=30))

# 时间替换
c_time = datetime.datetime.now()
print(c_time.replace(minute=20, hour=5, second=13))
