#!/usr/bin/python
#print('张禹')
# zy = "zhangyu"
# print(zy)
# n = zy
# print(n)
# zy = "张禹"
# print(zy)
# print(n)

# name = input("请输入姓名：")
# print(name)

# #引用加密模块
# import getpass
# pwd = getpass.getpass("请输入密码：")
# print(pwd)

# import getpass
# name = input("请输入姓名：")
# pwd = getpass.getpass("请输入密码：")
# print(name)
# print(pwd)

# if 1==1:
#     print('正确')
# else:
#     print('失败')

# import getpass
# name = input("请输入姓名：")
# pwd = getpass.getpass("请输入密码：")
# if name == "zhangyu" and pwd == "123456":
#     print("欢迎登陆")
# else:
#     print("账号或密码错误")

# user_name = input("请输入游戏：")
# if user_name == "魔兽世界":
#     print("玩了十年了")
# elif user_name == "英雄联盟":
#     print("万年青铜")
# else:
#     print("没时间玩游戏")
# print("很喜欢玩；但是；要养家")

# user_type = input("请输入游戏名称：")
# if user_type == "魔兽世界":
#     print("我很喜欢这个游戏")
#     user_name = input("请输入游戏账号：")
#     if user_name == "zhangyu":
#         print("我喜欢远程职业")
# else:
#     print("我很久不玩了")

# while True:
#     user = input("用户名：")
#     pwd = input("密码：")
#     if user == "zhangyu" and pwd == "123456":
#         print("登陆成功")
#         break#跳出循环
#     else:
#         print("用户名或密码错误")
# print("结束")

#输出1、2、3、4、5、6、8、9、10（没7）
# i = 1
# while True:
#     if i == 7:
#         i = i + 1
#         continue#这个单词下面有多少都不执行；从新开始循环
#     print(i)
#     i = i +1
#     if i == 11:
#         break#跳出所有循环

# i = 1
# value = 0
# while i < 101:
#     value = value + i
#     i = i + 1
# print(value)

# i = 1
# while i < 101:
#     yu = i%2
#     if yu == 0:
#         print(i)
#     i = i + 1

# i = 1
# while i < 101:
#     if i % 2 == 0:
#         print(i)
#     i = i + 1

# i = 1
# value = 0
# while i < 100:
#     if i % 2 == 1:
#         value += i#等于value = value + i
#     else:
#         value -= i
#     i += 1
# print(value)

# i = 0
# while i < 3:
#     user = input("用户名：")
#     pwd = input("密码：")
#     if user == "zhangyu" and pwd == "123456":
#         print("登陆成功")
#         break#跳出循环
#     else:
#         print("用户名或密码错误")
#     i += 1

# value = 7
# i = 0
# while i < 3:
#     num = input("请输入数字:")#输入的是字符串
#     num = int(num)#将字符串改变成数字类型
#     if value == num:
#         print("恭喜你；200元")
#         break
#     else:
#         print("再来一次")
#         i += 1

# #创建整数
# a = 123
# b = int(456)
# print(a,b)
# #转换整数
# c = "789"
# new_c = int(c)

#字符串
# a = "zhangyu"
# b = str("zhangyu-1")
# print(a)
# print(b)

# a = 19
# new_a = str(a)
# #type是查看数据的类型
# print(type(a))#a是数字；是类型
# print(type(new_a))#new_a是把a变成字符串类型

# user_name = "zhangyu"
# gender = "男"
# new_str = user_name+gender
# print(new_str)

# user_name = "姓名：张禹。性别：%s。%s岁。" %("男",30)
# print(user_name)

# content = "我叫张禹；爱玩游戏；魔兽世界和英雄联盟还有王者荣耀。"
# if "玩" in content:
#     print("爱玩的心；你不懂")
# else:
#     print(content)

# #移除字符串两边空白
# user_name = "  zhangyu   "
# print(user_name)
# new_str =  user_name.strip()#移除左右两边空白
# print(new_str)
# new_str_l = user_name.lstrip()#移除左边空白
# print(new_str_l)
# new_str_r = user_name.rstrip()#移除右边空白
# print(new_str_r)

# #分割
# user_name = "yaoshen|123456|9"
# #以又边一个“|”分割；分割成列表['yaoshen|123456', '9']
# new_user = user_name.rsplit("|",1)
# print(new_user)

# #长度（字符）
# user_name = "yaoshen|123456|9"
# new_user = len(user_name)
# print(new_user)

#索引
# user_name = "yaoshen|123456|9"
# print(user_name)#打印全部字符串
# print(user_name[0])#打印字符串的第1个字符
# print(user_name[1])#打印字符串的第2个字符
# print(user_name[2])#打印字符串的第3个字符
# print(user_name[3])#打印字符串的第4个字符
# print(user_name[4])#打印字符串的第5个字符

# #输入用户名并顺序打印
# user_name = input("请输入用户名：")
# i = 0
# while i < len(user_name):
#     print(user_name[i])
#     i += 1

# #切片
# content = "我叫张禹；爱玩游戏；魔兽世界和英雄联盟还有王者荣耀。"
# print(content[0])#打印第1个字符
# print(content[0:3])#打印第1到第3个字符
# print(content[0:9])#打印第1到第9个字符
# print(content[2:9])#打印第3到第9个字符
# print(content[9:])#打印第9到最后字符
# print(content[9:-1])#打印第9到最后第2个字符
# print(content[-1:])#打印最后1个字符
# print(content[-5:])#打印最后5个字符

#列表
# a = ["yao","shen",123456]
# if "shen" in a:
#     print(a)
# else:
#     print("不在里面")

# a = ["yao","shen",123456]
# print(a)
# print(a[0])
# print(a[1])
# print(a[2])

# a = ["yao","shen",123456]
# print(a)#['yao', 'shen', 123456]
# print(a[0])#yao
# print(a[1])#shen
# print(a[2])#123456
# print(a[0:2])#['yao', 'shen']
# print(a[1:3])#['shen', 123456]

# a = ["yao","shen",123456]
# a.append("妖神")#在列表的后面添加【妖神】
# print(a)
# a.insert(0,"A")#“0”表示在开头插入；
# a.insert(2,"B")#“2”表示在第2个位置插入【字符串计数是从0开始0、1、2、3】
# print(a)
# del a[4]#删除第4位置的123456
# print(a)
# a[1] = "YAO"#更改第1位置的yao为大写的YAO
# print(a)

# #for循环
# a = ["yao","shen",123456]
# for item in a:
#     print(item)

# #字典操作
# user_naem = {
#     "name": "yaoshen",
#     "password": "123456"
# }
# # #取出字典里的K和值
# # for k,v in user_naem.items():
# #     print(k)
# #     print(v)
# #     print("================")
# #简化写法
# for k,v in user_naem.items():print(k,v),print("================")

# #字典和列表的嵌套
# user_naem = {
#     "name": {"youxi":["魔兽世界","英雄联盟"],"password": "123456"}
# }
# print(user_naem)#打印完整的字典
# print(user_naem["name"])#打印字典name里的值
# print(user_naem["name"]["youxi"])#打印字典name里的youxi里的值
# print(user_naem["name"]["youxi"][0])#打印字典name里的youxi里的0位置的值
# print(user_naem["name"]["youxi"][1])#打印字典name里的youxi里的1位置的值
# print(user_naem["name"]["password"])#打印字典name里的password里的值

# #字典和列表的嵌套的增删改
# user_naem = {
#     "name": {"youxi":["魔兽世界","英雄联盟"],"password": "123456"}
# }
# print(user_naem)
# #在youxi里加入【王者荣耀】
# user_naem["name"]["youxi"].append("王者荣耀")
# print(user_naem)
# #在name字典里删除password
# del user_naem["name"]["password"]
# print(user_naem)
# #在name字典里加入age=30
# user_naem["name"]["age"] = 30
# print(user_naem)

# #多用户登录练习
# user_naem = [
#     {"name":"aaa","pwd":"123123","times":1},
#     {"name":"bbb","pwd":"123123","times":1}
# ]
# user = input("用户名：")
# pwd = input("密码：")
# for item in user_naem:
#     if user == item["name"] and pwd == item["pwd"]:
#         print("欢迎%s，登录成功" %(item["name"]))
#         break#因为字典里有很多用户信息；当用户名密码正确时；跳出所有循环
#     else:
#         print("用户名或密码错误，请重新登录。")
#         break#因为字典里有很多用户信息；当用户名密码错误时；跳出所有循环

#基本文件操作

















