# from collections import defaultdict
# def chi():
#     print("刘伟走了? 大阳哥来了")
#     return 123
# d = defaultdict(chi)
# print(d["jay"]) # dict()

# import time
# # print("大阳哥要睡觉了")
# # time.sleep(10)
# # print("大阳哥醒了")
# while 1:
#     s = time.strftime("%Y-%m-%d %H:%M:%S")
#     print(s)
#     time.sleep(1)

# 在这里之前。 很多模块已经导入进内存了。 自己的模块不要和python的模块冲突.
# import sys
# import builtins
# print(sys.path) # 搜索模块的路径, django . flask
# print(sys.modules.keys())
# sys.path.clear() # 寻找模块的路径给删了. 但是。 内存里的面的模块还在
# import json # 这里会报错.
# import os
# def copy(source, path):
#     path = os.path.join(path, os.path.basename(source))
#     with open(source, mode="rb") as f1, open(path, mode="wb") as f2:
#         for line in f1:
#             f2.write(line)
#
# copy("c:\\timg.jpg","d:\\")

# 计算时间差(用户输入起始时间和结束时间. 计算时间差(小时),
#  		例如, 用户输入2018-10-08 12:00:00   2018-10-08 14:30:00 输出2小时30分
# import time
# start_str = "2018-10-08 12:00:00"
# end_str = "2018-10-08 14:30:00"
#
# start_float = time.mktime(time.strptime(start_str, "%Y-%m-%d %H:%M:%S"))
# end_float = time.mktime(time.strptime(end_str, "%Y-%m-%d %H:%M:%S"))
#
# diff_second = end_float - start_float # 计算相差的秒数
#
# diff_min = diff_second // 60 # 计算出分钟  150
#
# show_hour = diff_min // 60
# show_min = diff_min % 60
#
# print(show_hour, show_min)

import random

# 获取[m, n]的随机整数

import os

