import time
# print(time.time()) # 当前系统时间 1538970854.5946708 float 时间戳. 给机器用的.数据库有的时候存储的是时间戳
# 以 1970-01-01 00:00:00 原点. 每一秒一个数字.

# 时间格式 格式化时间
# print(time.strftime("%Y/%m/%d %H:%M:%S")) # 给人看的.

# 结构化时间
# print(time.localtime())  # 用来计算的.


# 18888888888 时间戳 -> 格式化时间
# 把时间戳转化成结构化时间
# f = 18888888888
# st = time.localtime(f)
# print(st)
# # 格式化结构时间
# t = time.strftime("%Y/%m/%d %H:%M:%S",st) # f: format 格式化
# print(t)

# 用户输入了一个时间 2018-09-08 11:22:36   - 存储 时间戳
# 先把格式化时间转化成结构化时间
# s = "2018-09-08 11:22:36"
# st = time.strptime( s , "%Y-%m-%d %H:%M:%S") # p:parse 转换
# t = time.mktime(st) #  转化成时间戳 1536376956
# print(t)


# 时间差的计算.1. 用自己的办法解决问题. 2. 看我的那个代码.  研究.

print(time.asctime())

