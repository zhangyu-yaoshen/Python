#!/usr/bin/env python
# -*- coding:utf-8 -*-
#嵌套调用
# def my_max4(a,b,c,d):
#     res1=my_max2(a,b)
#     res2=my_max2(res1,c)
#     res3=my_max2(res2,d)
#     return res1,res2,res3
#
# def my_max2(x,y):
#     if x > y:
#         return x
#     else:return y
# print(my_max4(15,42,96,87))




#嵌套定义
x = 1
def f1():
    print("这是第一层")
    def f2():
        print("这是第二层")
        def f3():
            print("这是第三层")
            print(x)
        return f3
    return f2
func=f1()#进入第一层函数
func1=func()#进入第二层函数
func1()#进入第三层函数





