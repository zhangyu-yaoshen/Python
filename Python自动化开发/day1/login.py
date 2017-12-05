#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
yao|123123|0
shen|123123|0
基于文件存储的用户登录程序（3次登录失败，锁定用户）
"""
f1 = open("db","r")#以读的方式打开一个文件
data = f1.read()#给这个文件内容做变量
f1.close()#关闭这个文件
user_name = input("请输入用户名：")
user_pwd = input("请输入密码：")
user_info_list = []#建立空表，用来存放读取的数据
user_list = data.split("\n")#以换行符"\n"分割出每行数据
for item in user_list:
    temp = item.split("|")#以|分割；yao|123123|0
    user_dict = {
        "name":temp[0],
        "pwd":temp[1],
        "times":temp[2]
    }
    user_info_list.append(user_dict)  # 将user_dict字典导入空列表
for user_list in user_info_list:#循环这个表
    if int(user_list["times"]) < 3:#判断登录次数小于3次
        if user_name == user_list["name"]:#判断用户名
            if user_pwd == user_list["pwd"]:#判断密码
                print("欢迎%s登录" %(user_list["name"]))
                break#跳出循环
            else:#密码错误的话；增加一次登录次数
                user_list["times"] = int(user_list["times"]) + 1
                print("密码错误")
                break#跳出循环
    else:#登录次数大于3次；直接退出
        print("连续错误登录三次；请联系管理员")
        break
if user_name != user_list["name"]:#判断是否有这个用户
    print("没有这个用户")
new_list = []#建立新的空表；用于存放修改后的数据
for user_new in user_info_list:#循环这个新列表
    fg_user = (user_new["name"],user_new["pwd"],str(user_new["times"]))#拼接字符串；注意数据类型
    new_list.append("|".join(fg_user))
f2 = open("db","w")#以写的方式打开一个文件
f2.write("\n".join(new_list))#将列表写到文件里
f2.close#关闭文件
