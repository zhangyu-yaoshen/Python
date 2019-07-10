# 2，写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def func(lst):   # function
#     # return lst[1::2]
#
#     result = []
#     for i in range(len(lst)):
#         if i % 2 == 1:
#             result.append(lst[i])
#     return result

# 3, 写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
# def func(obj):
#     # if len(obj) > 5:
#     #     return True
#     # else:
#     #     return False
#     return len(obj) > 5


# 4, 写函数，检查传入列表的长度，如果大于2，将列表的前两项内容返回给调用者
# def func(lst):
#     if len(lst) > 2:
#         return lst[:2]


# 5, 写函数，计算传入函数的字符串中, 数字、字母、空格 以及 其他内容的个数，并返回结果 isalpha()
# def func(s=""):
#     shuzi = 0
#     zimu = 0
#     kongge = 0
#     qita = 0
#     for c in s:
#         if c.isalpha():
#             zimu = zimu + 1
#         elif c.isdigit():
#             shuzi = shuzi + 1
#         elif c.isspace():
#             kongge = kongge + 1
#         else:
#             qita = qita + 1
#     return shuzi, zimu, kongge, qita
#
# print(func("abcd1234@@@@    "))

# 6，写函数，接收两个数字参数，返回比较大的那个数字。
# def func(a, b):
#     # if a > b:
#     #     return a
#     # else:
#     #     return b
#     return a if a > b else b

# 三目运算
# a = 100
# b = 20
#
# c = a if a > b else b
# print(c)

# 7, 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# 	dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# 	PS:字典中的value只能是字符串或列表
# def func(dic):
#     for k, v in dic.items():
#         if len(v) > 2:
#             v = v[:2]
#             dic[k] = v
#     return dic

# 8, 8，写函数，此函数只接收一个参数且此参数必须是列表数据类型，
# 此函数完成的功能是返回给调用者一个字典，
# 此字典的键值对为此列表的索引及对应的元素。
# 例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。
# def func(lst):
#     if type(lst) != list:
#         print("扔出去一个异常")
#
#     dic = {}
#     for i in range(len(lst)):
#         dic[i] = lst[i]
#     return dic

# 写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，
# 然后将这四个内容传入到函数中，此函数接收到这四个内容，
# 将内容追加到一个student_msg文件中
# def func(name, age, edu, gender="男"):
#     f = open("student_msg", mode="a", encoding="utf-8")
#     f.write(name+"_"+gender+"_"+age+"_"+edu+"\n")
#     f.flush()
#     f.close()
#
# # func("郑中基", "男", "50", "大本")
# # func("张学友", "男", "60", "大本")
#
# while 1:
#     tiwen = input("请问是否要输入学生信息输入任意内容继续，输入Q退出：")
#     if tiwen.upper() == 'Q':
#         break
#
#     name = input("请输入你的姓名:")
#     gender = input("请输入你的性别:")
#     age = input("请输入你的年龄:")
#     edu = input("请输入你的学历:")
#
#     gender = "男" if gender == "" else "女"
#     func(name, age, edu, gender)

# 11 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（升级题）。
# import os
# def func(file_name, old, new):
#
#     with open(file_name, mode="r", encoding="utf-8") as f1, \
#         open(file_name+"_副本", mode="w", encoding="utf-8") as f2:
#         for line in f1:
#             line = line.replace(old, new)
#             f2.write(line)
#     os.remove(file_name)
#     os.rename(file_name+"_副本", file_name)


# 12. 写一个函数完成三次登陆功能，再写一个函数完成注册功能. 用户信息写入到文件中
#
# def regist(username, password): # wusir
#     # 1. 检查用户名是否重复
#     f = open("user_info", mode="r+", encoding="utf-8")
#     for line in f:
#         if line == "": # 防止空行影响程序运行
#             continue
#         user_info_username = line.split("_")[0]
#         if username == user_info_username: # 用户名重复了
#             return False
#     else:
#         # 2. 写入到文件中
#         f.write(username+"_"+password+"\n")
#
#     f.flush()
#     f.close()
#     return True
#
# name, psw = input("请输入你的用户名:"), input("请输入你的密码:")
# print(regist(name, psw))

# def login(username, password):
#     f = open("user_info", mode="r", encoding="UTF-8")
#     for line in f:
#         if line.strip() == username+"_"+password:
#             f.close()
#             return True
#     else:
#         f.close()
#         return False
#
# for i in range(2, -1, -1):
#     ret = login(input("请输入用户名:"), input("请输入密码:"))
#     if ret:
#         print("恭喜你. 登录成功")
#         break
#     else:
#         print("用户名或密码错误, 还有%s次机会" % i)
