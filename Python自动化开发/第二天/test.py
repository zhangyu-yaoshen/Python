#!/usr/bin/env python
# -*- coding:utf-8 -*-

# a = 123                                             #数字类的对象
# b = "sjdflskjf"                                   #字符串类的对象
# c = ["a","b","c"]                                 #列表类的对象
# d = {"name":"aaa","pwd":"123123","times":1}    #字典类的对象

##################################str字符串########################################
# name = "zhangyu"
# print(name.capitalize())#第一个字母大写Zhangyu

# name = "ZhangYu"
# print(name.casefold())#将字符串里的大写变小写。更好用

# name = "zhanagayu"
# print(name.count("a"))#统计a出现过几次

# name = "zhangyu"
# print(name.center(50,"-"))#打印50个字符zhangyu在中间；两边用-填充
# print(name.endswith("yu"))#判断以什么结尾；返回True
# print(name.expandtabs(tabsize=30))#将tab键转换成30个空格
# print(name.find("an"))#查找字符串的索引位
# name1 = "my name is {name} and is am {year}"
# print(name1.format(name="zhangyu",year=29))#将指定的值替换到指定的位置my name is zhangyu and is am 29
# print(name1.format_map({'name':'zhangyu','year':29}))#同上但很少用my name is zhangyu and is am 29
# print('abc123'.isalnum())#包含字母和数字
# print('abcG'.isalpha())#纯英文字符包括大小写
# print('9'.isdigit())#是否是整数
# print('aeee'.isidentifier())#判断是不是一个合法的标识符（变量）
# print('a12'.islower())#判断是不是小写
# print('12'.isnumeric())#判断只有数字字符，则返回真值
# print(' '.isspace())#判断是不是空格
# print('My Name Is Zhangyu'.istitle())#判断是不是开头
# print('My Name Is Zhangyu'.isprintable())#判断是否可以打印【用于tty和drive文件
# print('My Name Is Zhangyu'.isupper())#判断是否全是大写
# print(''.join(['1','2','3']))#join的用法是切割列表活字符串123
# print(','.join(['1','2','3']))#以逗号切割列表1,2,3
# print('='.join(['1','2','3']))#以等号切割列表1=2=3
# print(name.ljust(50,'*'))#长度50；不够的在后面补星号
# print(name.rjust(50,'='))#长度50；不够的在前面补等号
# print("Zhangy".lower())#把小写变大写
# print("Zhangy".upper())#把大写变小写
# print("   Zhangy   ".strip())#去掉两边的空格和回车
# print("   Zhangy   ".lstrip())#从左边去掉空格和回车
# print("   Zhangy   ".rstrip())#从左边去掉空格和回车
# p = str.maketrans("abcdef","123456")#逗号两边位数相同；用后面的代替前面的数值
# print("zhangyu".translate(p))#a用1代替；得到的值是zh1ngyu
# print("abcdefghi".translate(p))#得到的值是123456ghi
# print("zhangyau".replace('a','A'))#替换指定的值(zhAngyAu)
# print("zhangyau".replace('a','A',1))#替换指定的第一个值(zhAngyau)
# print("zhangyau".rfind('a'))#从左到右的查找最右边值所代表的标志位[6]
# print("zhangyau".split('a'))#以某个值为分隔符['zh', 'ngy', 'u']
# print("1=2=3=4=5=6=7=8=9".split('='))#['1', '2', '3', '4', '5', '6', '7', '8', '9']
# print("1=2=3=4\n5=6=7=8=9".splitlines())#识别不同系统的换行符['1=2=3=4', '5=6=7=8=9']
# #print(name.startswith())#startswith表示以什么开始
# print("zhangYU".swapcase())#表示大小写互换【ZHANGyu】
# print("zhangyu".title())#表示编程开头
# print("zhangyu".zfill(50))#补位；用0填充【用16进制补位】


























