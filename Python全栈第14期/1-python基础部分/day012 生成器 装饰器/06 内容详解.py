# -*- coding:utf-8 -*-
'''
@Author  : Python
@Time    : 2019/1/14 9:05
@Software: PyCharm
@File    : 03 内容详解.py
'''
#　装饰器　装饰的内容　　器工具　　装饰器：装饰的内容的一个工具
#  开放封闭原则    写代码要遵守

# 开发对扩展
# 修改源代码封闭
#不改变调用方式

# print(1000)
# def foo():
# 	print(1000)

# print(10)
# foo()  # 满足当前了
# print(100)
# foo()  # 100
# print(50)
# foo()  # 100

# import time
# # print(time.time())  #时间戳 1547428361.4262683  1547428402.3696105
# def func():
# 	time.sleep(2)  # 睡眠
# 	print(1000)
# f1 = func
#
# def foo():
# 	time.sleep(1)  # 睡眠
# 	print(100)
# 	# 修改源代码
# f = foo
#
# def timeer(x):
# 	stat_time = time.time()
# 	x()
# 	stop_time = time.time()
# 	print(stop_time - stat_time)
#
# foo = timeer
# foo(f)
#
# func = timeer
# func(f1)

# def func():  # 原函数
# 	time.sleep(2)
# 	print(1)



# import time  # 导入一个时间
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
# # 调用wapper
# foo = inner(foo)  # 自己实现的  python中帮咱们实现了这个  @语法糖
# foo()



import time  # 导入一个时间
def inner(func):  # 闭包  func现在就是foo的内存地址
	#　定义一个函数
	x = func  #　把foo的内存地址赋值给了x   x就是foo的内存地址
	# 把func形参赋值个x变量
	def wapeer():
		#　定义一个函数
		s_time = time.time()
		x()  #就是执行foo()
		ss_time = time.time()
		print(ss_time - s_time)
	return wapeer    #定义函数的时候，下边的代码是返回这个函数的内存地址　
	# 把函数名当做值返回
@inner   # foo = inner(foo)  #被装饰的函数正上方加一个@装饰器的名字
def foo():
	print('is foo')
foo()
foo = inner(foo)  # 先执行等号的右边



# import time  # 导入一个时间
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
# 	return wapeer           #定义函数的时候，下边的代码是返回这个函数的内存地址　
# 	# 把函数名当做值返回
# @inner   # foo = inner(foo)  #被装饰的函数正上方加一个@装饰器的名字
# def foo():
# 	print('is foo')
# foo()



# def inner(func):   # 1010
# 	def wapeer(*args,**kwargs): # 01010101   *args,**kwargs 聚合
# 		func(*args,**kwargs)  # 010101()     *args,**kwargs 打散
# 	return wapeer # 01010101

# @inner  # num_sum = inner(num_sum)
# def num_sum(*args,**kwargs):  #num_sum内存地址 010101   *args,**kwargs 聚合
# 	print(*args)
# num_sum(5,4,5,6,7,8,9,)  #01010101(5,4)

# 有参装饰器 有能力尝试


# def inner(func):   # 1010
# 	def wapeer(*args,**kwargs): # 01010101   *args,**kwargs 聚合
# 		print('开始看上棒哥')
# 		func(*args,**kwargs)  # 010101()     *args,**kwargs 打散
# 		print('棒哥看不上我')
# 	return wapeer # 01010101
#
# def inner2(func):   # 1010
# 	def wapeer2(*args,**kwargs): # 01010101   *args,**kwargs 聚合
# 		print('开始追姑娘了')
# 		func(*args,**kwargs)  # 010101()     *args,**kwargs 打散
# 		print('还没开始就结束了')
# 	return wapeer2 # 01010101
#
# @inner
# @inner2
# def foo():
# 	print(1)
# foo()

#总结:
# 装饰器本质就是闭包
# 装饰器中的语法糖 必须单独占一行
#  遵守开放封闭原则,并且不能修改调用方式
#  开发对扩展
#　封闭修改源代码
#  装饰器的应用:
# 		不能说测试函数运行时间
# 		增加一些功能
# 		校验用户登录的时候  Django   面向对象
# 语法糖  的本质  被装饰的函数名 = 装饰器的名字(被装饰的函数名)


# print(abs(-10))   # 绝对值
# print(all([1,2,3,4,5]))  #都为真才是真
# print(any([0,0,1]))   # 有一个为真就是真

# print(ascii('你好'))  # 在ascii中原生显示,\u...

# b = bytearray('你好啊',encoding='utf-8')
# print(b[0])

# l = bytes('你好啊',encoding='gbk')
# print(str(l,encoding='gbk'))

# name = 'alex'
# def foo():
# 	pass
# #判断是否可调用
# print(callable(foo))

# print(chr())  # 对应ascii码  码位对应的内容

# print(complex('12312321'))

# li = ['a','b','c','d']
# for i,em in enumerate(li):  ###经常用到
# 	print(i,em)

# enumerate('可迭代对象','默认不写的时候是0',自己定义起始值)

# s = input(">>>")
# li = ['del','remove','clear','你傻逼']
# if s in li:
# 	pass
# else:

# 	print(eval(s))  # 执行部分字符串中的内容  容易出事  开发中禁止使用
# exec(s)           # 执行字符串中的内容      更容易出事  开发中更禁止使用


# print(float(100))

# format()  #内置函数
# ''.format()  #字符串方法

# print(format('meet','>40')) #右对齐
# print(format('meet','<40')) #左对齐
# print(format('meet','^40')) # 居中

# print(hash())  # 来确认那些数据可以当做字典的键  有值就是可以

# print(help(format))  # 帮助咱们查看的方法

# print(max({1:333,3:5656})) 最大值
# print(min())               最小值
# print(sum())                 求和

# print(sum([1,2345]))

# def sum(*args):
# 	count = 0
# 	for i in args:
# 		count += i
# 	return count

# print(sum('123'))

# print(memoryview(b'alex'))  # 求字节的内存地址

# print(ord('你'))  #　写内容查看ｕｎｉｃｏｄｅ的表位

# print(pow(2,3))     求幂
# print(pow(2,3,3))   求幂后再取余

# print('你好',end='')  # print(end='\n')
# print('我好')
# print('大家好')

# print('你好','我好',sep='   ')

# s = '[1,2,3]'
# print(repr(s))  # 显示数据的原生
# print(s)  # 显示数据的原生\

# l = reversed('123')  # 反转  迭代器
# for i in l:
# 	print(i)
# print(list(l))

# print(list('123'))   # 工厂

# print(round(3.332324,3))  #四舍五入　第一个参数是浮点数　　第二参数的要保留的小数位


# print(list(123))

# def lst(args):
# 	li = []
# 	for i in args:
# 		li.append(i)
# 	return li
# print(lst(123))

# lst = [1,2,3,4]
# print(lst[slice(0,2)])   #切片
# print(lst[0:2])

# lst = [22,2,3,4]   # 左边牙
# lst1 = {'1':2,'3':4}     # 右边牙
# lst2 = [4444,2,3,4,5]
# for i in zip(lst,lst1,lst2): # 拉锁  如果长度不统一的时候按照短的来
# 	print(i)

# 匿名函数:  没有名字 的函数

# lambda 关键字 x 变量形参 : 返回值

# def func(xx):
# 	return  xx + xx
#
# print(func.__name__)

# f = lambda x:x+x
# print(f(3))   # f是函数的名字吗????

# f = lambda x:x+x
# print(f.__name__)   #<lambda>

# print((lambda x:x+x)(3))

# print((lambda x,y,c:(x,y,c))(1,2,3))


# 匿名函数的时候定义和函数 没有def 没有函数名
# 有形参,形参可以接受多个
# 返回值只能用一个
# 匿名函数时没有名字的,赋值的变量只是方便咱们调用的时候
# ls = [1,2,3,4]
# dic = {1:2,2:3}
# def func(ls):
# 	lst = []
# 	for i in ls:
# 		lst.append(i**i)
# 	return lst
# print(sorted(func(ls),reverse=True))
# print(sorted(dic.values(),reverse=True))
# print(sorted({1:2,2:3},reverse=False))    #第一个参数是可迭代对象 ,默认是升序  降序reverse=True


# lst = ['策哥','老牛逼了','静哥','老厉害了','小强打不死']
#
# def foo(x):
# 	return len(x)
#
# print(sorted(lst,key=foo))  #key是一种排序的规则  不写的话就以数字的大小去排序  写了就按照规则

# def foo(x):
# 	if x > 1:
# 		return x
#
# lst = [1,2,3,4,5,6,7]
#
# dic = [{'name':'alex','age':19},{'name':'wusir','age':16}]
# print(list(filter(lambda x:x['age']>17,dic)))

# print(list(filter(foo,lst)))

# lst = [1,2,3,4]
#
# def func():
# 	for i in lst:
# 		print(i**2)
# func()
#
# def func(x):
# 	return x**2
# print(list(map(func,lst)))
#
# print(list(map(lambda x:x**x+1,lst)))



# lst = [2,3,4,5]
# lst1 = [3,4,5,6]   # [5,7,9,11]
#
# print(list(map(lambda x,y:x+y,lst,lst1)))
#
# from functools import reduce  # python3导入方式
# # import reduce  #python2
# lst = [2,3,4]
# print(reduce(lambda x,y:x**y,lst))  # 累  计算
# print(lst)

# 递归: 明天讲

