import configparser

# conf = configparser.ConfigParser()
# conf["DEFAULT"] = {
#     "session-time-out":30,
#     "user-alive": 60,
#     "connect-alive":10
# }
#
# conf["189-DB"] = {
#     "ip": "189.135.63.12",
#     "port": 3306,
#     "uname": "root",
#     "password": "root"
# }
#
#
# conf["166-DB"] = {
#     "ip": "189.135.63.12",
#     "port": 3306,
#     "uname": "root",
#     "password": "root"
# }
#
#
# conf["163-DB"] = {
#     "ip": "189.135.63.12",
#     "port": 3306,
#     "uname": "root",
#     "password": "root"
# }
#
# f = open("db.ini", mode="w")
# conf.write(f) # 把文件扔进去。 写到这个文件里


# # 读取内容
# conf = configparser.ConfigParser()
# conf.read("db.ini")
# print(conf.sections()) # 获取到章节 keys()
# print(conf['166-DB']["ip"])  # 可以像字典一样操作
# print(conf["166-DB"]["port"])
# print(conf["166-DB"]["uname"])
# print(conf["166-DB"]["password"])
#
# for key in conf['163-DB']:
#     print(key)
#
# for key, value in conf['163-DB'].items():
#     print(key, value)


# # # 增删改操作
conf = configparser.ConfigParser()
conf.read("db.ini") # 读取出来

# conf['163-DB']['uname'] = "alex"#将163-DB的name修改成alex
# del conf['163-DB']["password"]
# conf.set("163-DB", "wangermazi", "189") # setattr

conf.add_section("jay")
conf.write(open("db.ini", mode="w"))


