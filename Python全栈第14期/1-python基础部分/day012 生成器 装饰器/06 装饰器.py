#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Name    : 06 装饰器.py
Author  : Python
Time    : 2019/7/18 0018 16:52
"""
# 装饰器：装饰内容的一个工具
# 开放封闭原则    写代码要遵守
# 开发对扩展，修改源代码封闭，不改变调用方式

# import time
#print(time.time())#时间戳

# def timeer(x):
#     start_time = time.time()
#     x()
#     stop_time = time.time()
#     print(stop_time - start_time)
#
# @timeer
# def foo():
#     time.sleep(1)
#     print("魔兽世界")
# foo()



# import time
# def func():  # 原函数
# 	time.sleep(2)
# 	print("魔兽世界")
#
# def inner(func):  # 闭包
# 	#　定义一个函数
# 	x = func
# 	# 把func形参赋值个x变量
# 	def wapeer():
# 		#　定义一个函数
# 		s_time = time.time()
# 		x()
# 		ss_time = time.time()
# 		print(ss_time - s_time)
# 	return wapeer
# 	# 把函数名当做值返回
# func = inner(func)
# #　首先要调用inner函数func的内存地址当做实参传递给形参
# # func 是调用inner函数时的返回值   func就是wapeer函数
# func()













# import time
# def inner(func):  # 闭包  func现在就是foo的内存地址
# 	#　定义一个函数
# 	x = func  #　把foo的内存地址赋值给了x   x就是foo的内存地址
# 	# 把func形参赋值个x变量
# 	def wapeer():
# 		#　定义一个函数
# 		s_time = time.time()
# 		x()  #就是执行foo()
# 		ss_time = time.time()
# 		print(ss_time - s_time)
# 	return wapeer    #定义函数的时候，下边的代码是返回这个函数的内存地址　
# 	# 把函数名当做值返回
# @inner   # foo = inner(foo)  #被装饰的函数正上方加一个@装饰器的名字
# def foo():
#     time.sleep(2)
#     print("魔兽世界")
# foo()
# # foo = inner(foo)  # 先执行等号的右边

# def inner(func):   # 1010
# 	def wapeer(*args,**kwargs): # 01010101   *args,**kwargs 聚合
# 		func(*args,**kwargs)  # 010101()     *args,**kwargs 打散
# 	return wapeer # 01010101
#
# @inner  # num_sum = inner(num_sum)
# def num_sum(*args,**kwargs):  #num_sum内存地址 010101   *args,**kwargs 聚合
# 	print(*args)
# num_sum(5,4,5,6,7,8,9,)  #01010101(5,4)
# # 有参装饰器 有能力尝试

def inner(func):   # 1010
	def wapeer(*args,**kwargs): # 01010101   *args,**kwargs 聚合
		print('开始看上棒哥')
		func(*args,**kwargs)  # 010101()     *args,**kwargs 打散
		print('棒哥看不上我')
	return wapeer # 01010101

def inner2(func):   # 1010
	def wapeer2(*args,**kwargs): # 01010101   *args,**kwargs 聚合
		print('开始追姑娘了')
		func(*args,**kwargs)  # 010101()     *args,**kwargs 打散
		print('还没开始就结束了')
	return wapeer2 # 01010101

@inner
@inner2
def foo():
	print(1)
foo()