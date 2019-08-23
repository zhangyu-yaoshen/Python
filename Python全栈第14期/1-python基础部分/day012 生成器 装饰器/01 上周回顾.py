# -*- coding:utf-8 -*-
'''
@Author  : Python
@Time    : 2019/1/14 8:39
@Software: PyCharm
@File    : 01 上周回顾.py
'''
# 1.生成器
# 函数中yield的就是生成器,生成器的本质就是迭代器
# yield 可以写多个 最后一个yield下边的代码不会执行

# yield from  可迭代对象
# 将可迭代对象的每个元素返回
# send() # 启动yield时 传值给上一个yield

# 2.推导式
# 列表推导式
# l = [结果 for i in 可迭代对象]

# 集合推导式:
# s = set(结果 for i in 可迭代对象)
# s = {结果 for i in 可迭代对象}

# 字典推导式:
# dic = {k:v for k,v in 可迭代对象}

# 生成器推导式:
# s = (结果 for i in 可迭代对象)

# 筛选:
# l = [结果 for i in 可迭代对象 条件语句]
# 所有的推导式都可以使用


# 在函数内部,调用外部变量(非全局变量)的函数就是闭包:

# print(100)
#
# def func():
# 	name = '宝宝'
# 	def fuck():
# 		print(name)
# 	return fuck
#
# f = func
#
# def foo(*args,**kwargs):
# 	pass
#
# foo(f)
#
# # 函数的使用:
# f = func

# def func():
# 	pass
#
# print(func)
#
# print(100)
# f()
# print(100)
# f()

# 此时此刻是闭包吗?
# 部分面试官:
# 1.在嵌套的函数内
# 2.调用外部变量(非全局变量)的函数
# 3.将内部函数名返回

