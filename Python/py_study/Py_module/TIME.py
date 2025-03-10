#################################################################################################
#################################################################################################
"""

TIME module
Python 的 time 库提供了处理时间和日期的基础功能，包括获取时间戳、格式化时间、延时操作等

"""
#################################################################################################

import time



# 获取时间戳
# time.time()
# 返回自纪元（Epoch，即 1970 年 1 月 1 日 00:00:00 UTC）以来的秒数
# 通常用于计算时间差
current_time = time.time()

print(current_time) # 输出类似 1741603069.5025134
print("-------------------------------------------------")


# time.localtime() 和 time.gmtime()
# 分别返回本地时间和 UTC 时间的结构体
local_time = time.localtime()
utc_time = time.gmtime()

print(local_time)
print(utc_time)
print("-------------------------------------------------")
# time.struct_time(tm_year=2025, tm_mon=3,
#                  tm_mday=10, tm_hour=18,
#                  tm_min=39, tm_sec=39,
#                  tm_wday=0, tm_yday=69,
#                  tm_isdst=0)
# time.struct_time(tm_year=2025, tm_mon=3,
#                  tm_mday=10, tm_hour=10,
#                  tm_min=39, tm_sec=39,
#                  tm_wday=0, tm_yday=69,
#                  tm_isdst=0)


# tm_year	年	例如 2023
# tm_mon	月	1-12
# tm_mday	日	1-31
# tm_hour	小时	0-23
# tm_min	分钟	0-59
# tm_sec	秒	0-61（闰秒）
# tm_wday	星期几（0=周一）	0-6
# tm_yday	一年中的第几天	1-366
# tm_isdst	是否夏令时	-1, 0, 1


# time.strftime(format, time_tuple)
# 可以将时间结构体格式化为字符串
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(formatted_time)  # 2025-03-10 18:44:18
print("-------------------------------------------------")
# %Y：四位年份（如 2023）
# %m：两位月份（01 到 12）
# %d：两位日期（01 到 31）
# %H：两位小时（24 小时制，00 到 23）
# %M：两位分钟（00 到 59）
# %S：两位秒数（00 到 59）


# time.strptime(time_string, format)
# 可以将时间字符串解析为时间结构体
time_string = "2023-01-01 00:00:00"
parsed_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print(parsed_time)
print("-------------------------------------------------")
# time.struct_time(tm_year=2023, tm_mon=1,
#                  tm_mday=1, tm_hour=0,
#                  tm_min=0, tm_sec=0,
#                  tm_wday=6, tm_yday=1,
#                  tm_isdst=-1)


# time.sleep(seconds)
# 用于暂停程序执行指定的秒数
print("Start")
time.sleep(2)  # 暂停 2 秒
print("End")
print("-------------------------------------------------")


# 时间戳与结构化时间的相互转化
# 结构化时间 → 时间戳
timestamp = time.mktime(local_time)
# 时间戳 → 结构化时间
struct_time = time.localtime(timestamp)

print(timestamp)
print(struct_time)
# 1741604071.0
# time.struct_time(tm_year=2025, tm_mon=3,
#                  tm_mday=10, tm_hour=18,
#                  tm_min=54, tm_sec=31,
#                  tm_wday=0, tm_yday=69,
#                  tm_isdst=0)
print("-------------------------------------------------")


print("-------------------------------------------------")

#################################################################################################
#################################################################################################