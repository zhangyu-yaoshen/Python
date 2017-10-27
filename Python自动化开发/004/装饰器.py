#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
统计函数运行时间的装饰器
"""
import time
def timmer(func):#装饰器开始
    def warpper(*args,**kwargs):
        print("这是开始")
        start_time=time.time()
        func()#运行zhangyu函数
        stop_time=time.time()
        print("统计函数的运行时间是：%s" %(stop_time-start_time))
    return warpper#装饰器结束
@timmer#调用装饰器
def zhangyu():
    time.sleep(3)#sleep延迟执行
    print("in the zhangyu")
zhangyu()









