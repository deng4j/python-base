import time

"""
时间元组：
    0	tm_year：4位数年	        2008
    1	tm_mon：月	                1到12
    2	tm_mday：日	                1到31
    3	tm_hour：小时	            0到23
    4	tm_min：分钟	            0到59
    5	tm_sec：秒	                0到61(60或61 是闰秒)
    6	tm_wday：一周的第几日	    0到6(0是周一)
    7	tm_yday：一年的第几日	    1到366(儒略历)
    8	tm_isdst：夏令时	        -1, 0, 1, -1是决定是否为夏令时的标识
    
python中时间日期格式化符号：
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00=59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称
    %% %号本身
"""

print("----------------------------- 时间戳 --------------------------------\n")

time_stamp = time.time()  # 时间戳
print("时间戳：{}".format(time_stamp))

print("----------------------------- 格式化时间 --------------------------------\n")

format_time = time.strftime("%Y-%m-%d %X")
print("格式化时间：{}".format(format_time))

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

print("----------------------------- 结构化的时间 --------------------------------\n")

# 结构化的时间(struct time)：struct_time元组共有9个元素共九个元素，分别为(年，月，日，时，分，秒，一年中第几周，一年中第几天，夏令时)
print('构化时间的基准时间:{}'.format(time.localtime(0)))
print('本地时区的struct_time:{}'.format(time.localtime()))
print('UTC时区的struct_time:{}'.format(time.gmtime()))

# 结构化时间的基准时间上增加一年时间
print(time.localtime(3600 * 24 * 365))
