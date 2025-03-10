#################################################################################################
#################################################################################################
"""

DATETIME
Python的datetime库是标准库中处理日期和时间的核心模块
提供了日期、时间、时间差及时区操作的功能

"""
#################################################################################################
"""

datetime 类
日期和时间的组合，最常用的类

"""
#################################################################################################

from datetime import datetime



# datetime.now()
# 当前本地时间
print(datetime.now()) # 2025-03-10 19:09:14.039131


# datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
# 自主创建时间
dt = datetime(2021, 11, 13, 7, 38, 53)
print(dt) # 2021-11-13 07:38:53
print(type(dt)) # <class 'datetime.datetime'>


# datetime.strptime(string, format)
# 解析自定义格式字符串
dt_parsed = datetime.strptime("2023-10-05", "%Y-%m-%d")


# 对于所有的 datetime 类，都可以使用 .hour, .minute 等来获取特殊需求
dt = datetime(2021, 11, 13, 7, 38, 53)
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
# 2021 11 13 7 38 53

#################################################################################################
"""

time 类
处理时间（不含日期）

"""
#################################################################################################

from datetime import time



# 一般创建方法
# time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
t = time(3, 4,3)
print(t) # 03:04:03
print(type(t)) # 类型 <class 'datetime.time'>


# .hour, .minute, .second
t = time(3, 4,3)
print(t.hour, t.minute, t.second)  # 14 30 15


# 自定义格式
t = time(3, 4,3)
print(t.strftime("%H %M %S"))  # 03 04 03

#################################################################################################
"""

date 类
处理日期（不含时间）

"""
#################################################################################################

from datetime import date



# 一般创建方式
# date(year, month, day)
d = date(2121, 5, 9)
print(d) # 2121-05-09
print(type(d)) # <class 'datetime.date'>


# date.today()
# 获取当前本地日期
print(date.today()) # 2025-03-10


# .year, .month, .day, .weekady
d = date(2121, 5, 9)
print(d.year, d.month, d.day)  # 输出: 2121 5 9
print(d.weekday())    # 4  返回0-6（0=周一）


# strftime
# 自定义格式
d = date(2121, 5, 9)
print(d.strftime("%Y/%m/%d"))  # 2121/05/09

#################################################################################################
"""

timedelta 类
表示时间间隔，用于日期/时间的加减操作

"""
#################################################################################################

from datetime import datetime, timedelta



# 一般创建方式
# timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
dt = datetime.now()
delta = timedelta(days=5, hours=3)
future = dt + delta  # 5天3小时后的时间
past = dt - delta    # 5天3小时前的时间


# 计算时间差
diff = future - past  # 结果为 timedelta(days=10, hours=6)

#################################################################################################
#################################################################################################