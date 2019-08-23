# 电影投票. 程序先给出⼀个⽬前正在上映的电影列表.
# 由⽤户给每⼀个电影投票. 最终 将该⽤户投票信息公布出来
# lst = ['⾦瓶梅', '解救吾先⽣', '美国往事', '⻄⻄⾥的美丽传说']
# 结果: {'⾦瓶梅': 99, '解救吴先⽣': 80, '美国往事': 6, '⻄⻄⾥的美丽传说': 23}
# lst = ["头号玩家", "爱情公寓", "一出好戏", "西虹市首富"]
# dic = {}
# for el in lst: # 每一个电影, "头号玩家"
#     fen = input("请给<%s>电影打分:" % el)
#     dic[el] = int(fen)
#
# print(dic)


# 3.念数字.  给出一个字典. 在字典中标识出每个数字的发音. 包括相关符号.
# 然后由用户输入一个数字. 让程序读出相对应的发音(不需要语音输出. 单纯的打印即可)
# dic = {
#     "-": "fu",
#     "1": "yi",
#     "2": "er",
#     "3": "san",
#     "4": "si",
#     "5": "wu",
#     "6": "liu",
#     "7": "qi",
#     "8": "ba",
#     "9": "jiu",
#     "0": "ling",
#     ".": "dian"
# }
# num = input("请输入你要读的数字:")    # 1.25
# s = ""
# for c in num:
#     s = s + dic[c] + " "
# print(s)


# 4.车牌区域划分, 现给出以下车牌. 根据车牌的信息, 分析出各省的车牌持有量.
# cars = ["鲁A 10086", "黑A 45678", "黑C 12345", "京B 00001", "京C 78912", "京A 66666"]
# locations = {"鲁": "山东", "黑": "黑龙江", "京": "北京", "沪": "上海"}
# dic = {}
#
# for car in cars: # 每个车牌子 鲁A 10086
#     paitou = car[0] # 鲁
#     # if dic.get(locations[paitou]) == None:
#     #     dic[locations[paitou]] = 1
#     # else:
#     #     dic[locations[paitou]] = dic[locations[paitou]]+1
#
#     # 省份 # "山东": 1, "黑龙江":1
#     # num = dic.get(locations[paitou], 0)
#     # num = num + 1
#     # dic[locations[paitou]] = num
#
#     dic[locations[paitou]] = dic.setdefault(locations[paitou], 0) + 1
#
# print(dic)

zhubo = {"旭旭宝宝": 99999999, "轩墨宝宝": 56565656, "alex": 2, "wusir": 60, "金老板": 60000, "卢本伟": 99999999}
s = 0
for value in zhubo.values():
    s += value
avg = s/len(zhubo)
print(avg)

# zhubo.pop("卢本伟")
# print(zhubo)

# 需要找一个列表把要删除的内容记录下来
lst = []
for k, v in zhubo.items():
    if v < avg:
        lst.append(k) # 把要删除的主播. 记录下来

for el in lst:
    zhubo.pop(el)

print(zhubo)







# result = {"山东": 1, "黑龙江":2, "北京":3}



