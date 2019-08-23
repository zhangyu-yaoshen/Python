# wf = {
#     "name": "汪峰",
#     "age": 18,
#     "hobby": "抢头条",
#     "wife": {
#         "name": "子怡",
#         "age": 19,
#         "hobby":["唱歌", "跳舞", "演戏"]
#     }
# }
#
# wf['wife']['hobby']
# class Person:
#     def __init__(self, name, age, hobby, wife):
#         self.name = name

import json
dic = {"a": '理查德姑妈', "b": "找到你", "c": "看不见的客人"}
#
# # s = json.dumps(dic) # 如果你的key或者value超出了ascii范畴。 就会显示成\uxxxxx
# s = json.dumps(dic, ensure_ascii=False) # 干掉ascii码
# print(repr(s), type(s))
# #
# #
# # 把字符串解析成 字典
# dic1 = json.loads(s)
# print(dic1, type(dic1))

# # 写入
# f = open("waimai.json", mode="w", encoding="utf-8")
# json.dump(dic, f, ensure_ascii=False)   # 把json写入到文件中
# f.close()
# #
# # 读出
# f = open("waimai.json", mode="r", encoding="utf-8")
# s = json.load(f) # 把文件中的json串。读取成字典
# print(s, type(s))

# lst = [{"a": "胡辣汤"},{"b":"吱吱冒油的大猪蹄子"},{"c": "盖浇饭"},{"d":"马拉"},{"e":"法国大蜗牛"}]
# f = open("menu.json", mode="w", encoding="utf-8")
# for dic in lst:
#     json.dump(dic, f, ensure_ascii=False)
# f.close()
#
# f = open("menu.json", mode="r", encoding="utf-8")
# s = json.load(f)
# print(s)

# 写入的时候
# 1. 循环
# 2. 用dumps把字典转化成字符串， 然后手工在后面加一个\n
# 3. 写出
f = open("new_menu.json", mode="w", encoding="utf-8")
lst = [{"a": "胡辣汤"},{"b":"吱吱冒油的大猪蹄子"},{"c": "盖浇饭"},{"d":"马拉"},{"e":"法国大蜗牛"}]
for el in lst:
    s = json.dumps(el, ensure_ascii=False) + "\n"
    f.write(s)
f.flush()
f.close()


# 读取的时候
# 1. for line in f:
# 2. strip()去掉空白
# 3. loads()变成字典

f = open("new_menu.json", mode="r", encoding="utf-8")
for line in f:
    line = line.strip()
    dic = json.loads(line)
    print(dic)
