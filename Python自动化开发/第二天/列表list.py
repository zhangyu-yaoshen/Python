#!/usr/bin/env python
# -*- coding:utf-8 -*-
##################################【list列表】########################################
# 1、追加
# user_list = ["aa","bb","cc"]
# v = user_list.append("dd")
# print(user_list)
# 2、清空
# user_list = ["aa","bb","cc"]
# user_list.clear()
# print(user_list)
# 3、复制【浅拷贝】
# user_list = ["aa","bb","cc"]
# v = user_list.copy()
# print(user_list)
# print(v)
# 4、计数
# user_list = ["aa","bb","aa","cc"]
# v = user_list.count("aa")
# print(v)
# 5、扩展【把一个列表添加到另一个列表】
# user_list = ["aa","bb","cc"]
# user_list.extend(["dd","ee","ff"])
# print(user_list)
# 6、查找索引,没有报错
# user_list = ["aa","bb","cc"]
# v = user_list.index("bb")
# print(v)
# 7、删除并且获取元素
# user_list = ["aa","bb","cc"]
# v = user_list.pop(1)#把要删除的元素赋值给v
# print(v)
# print(user_list)
# 8、删除
# user_list = ["aa","bb","cc"]
# v = user_list.remove("bb")
# print(v)
# print(user_list)
# 9、反转
# user_list = ["aa","bb","cc"]
# user_list.reverse()
# print(user_list)
# 10、排序
# nums = [9,88,77,6,555,44,3,2,12,1]
# print(nums)
# nums.sort()#从小到大排序
# print(nums)
# nums.sort(reverse=True)#从大到小排序
# print(nums)
# # range
# for i in range(10,0,-1):#倒序；减一
#     print(i)
# 从1开始打印变量序号
szj_list = ["人之初","性本善","性相近","习相远"]
for index,i in enumerate(szj_list,1):#index是索引；i是后面的变量
    print (index,i)









