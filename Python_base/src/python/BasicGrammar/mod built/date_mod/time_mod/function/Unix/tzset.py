import time
import os

"""
tzset() 根据环境变量TZ重新初始化时间相关设置。# Unix only

std offset [dst [offset [,start[/time], end[/time]]]]：
    std 和 dst:三个或者多个时间的缩写字母。传递给 time.tzname.
    offset: 距UTC的偏移，格式： [+|-]hh[:mm[:ss]] {h=0-23, m/s=0-59}。
    start[/time], end[/time]: DST 开始生效时的日期。格式为 m.w.d — 代表日期的月份、周数和日期。
        w=1 指月份中的第一周，而 w=5 指月份的最后一周。'start' 和 'end' 可以是以下格式之一：
            Jn: 儒略日 n (1 <= n <= 365)。闰年日（2月29）不计算在内。
            n: 儒略日 (0 <= n <= 365)。 闰年日（2月29）计算在内
            Mm.n.d: 日期的月份、周数和日期。w=1 指月份中的第一周，而 w=5 指月份的最后一周。
            time:（可选）DST 开始生效时的时间（24 小时制）。默认值为 02:00（指定时区的本地时间）。
"""

os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
time.tzset()
print(time.strftime('%X %x %Z'))

os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
time.tzset()
print(time.strftime('%X %x %Z'))
