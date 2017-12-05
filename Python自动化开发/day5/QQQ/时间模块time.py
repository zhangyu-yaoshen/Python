#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
# print(time.asctime())#当前的系统时间
# t = time.localtime()#可以按照自己的需求打印时间
# #time.struct_time(tm_year=2017, tm_mon=11, tm_mday=2, tm_hour=11, tm_min=7, tm_sec=5, tm_wday=3, tm_yday=306, tm_isdst=0)
# print(t)
# print(t.tm_year,t.tm_mon)#打印年和月

# #自定义时间展示格式
# struct_time = time.localtime(time.time() - 86400)#当前时间减去一天
# print(time.strftime("%Y-%m-%d %H:%M:%S"))#【2017-11-02 11:29:29】
# print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time))#打印一天前的时间
# s_time= time.strptime("2017-11-02","%Y-%m-%d")#将字符串转换成时间格式
# print(time.mktime(s_time))#转换成时间戳


import datetime
#时间的加减
print(datetime.datetime.now())#当前时间
print(datetime.datetime.fromtimestamp(time.time()))#时间戳直接转换成日期格式
print(datetime.datetime.now() - datetime.timedelta(days=5))#减5天
print(datetime.datetime.now() + datetime.timedelta(days=5))#加5天
print(datetime.datetime.now() - datetime.timedelta(days=5,hours=5,minutes=10))#减5天5小时10分钟

#时间的替换
print(datetime.datetime.now().replace(year=2016,month=3))#替换成2016年3月




