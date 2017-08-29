#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
yao|123123|0
shen|123123|0
1、读取文件；db文件里的数据有很多行；
2、以换行符分割出每行数据
"""
f1 = open("db","r")#以读的方式打开一个文件
data = f1.read()#给这个文件内容做变量
f1.close()#关闭这个文件
print(data)
#建立空列表
user_info_list = []
#以换行符"\n"分割出每行数据
user_list = data.split("\n")
print(user_list)
for item in user_list:
    temp = item.split("|")#以|分割；yao|123123|0
    user_dict = {
        "name":temp[0],
        "pwd":temp[1],
        "times":temp[2]
    }
    user_info_list.append(user_dict)#将user_dict字典导入空列表
user_info_list[1]["times"] = 3#修改shen的times值
print(user_info_list)


