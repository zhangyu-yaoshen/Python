# name = "ableX eggon eve_j leNb"
#
# count = 0
# while count < len(name):
#     if name[count] == 'e':
#         print(count)
#     count += 1

# for c in name: # char  charactor   你没有索引
#     if c == 'e':
#         name.find(c)


# print(name.strip("ab")) # 迭代进行匹配 ???????

# print(name.lstrip("a").rstrip("b"))


# s = "123a4b5c" # "2ab"
# print(s[1:-2:2])
# print(s[-3::-2])

# s="abcdefg"
# for c in s:
#     print(c, "sb")
#
# print("周杰伦", "周润发", "周星驰")



# s = "321"
# for c in s:
#     print("倒计时%s秒" % (c))
# else:    # for执行完毕。 最终收尾是else
#     print("出发")

# content = input("请输⼊内容:") ⽤户输⼊：5+9或5+ 9或5 + 9，然后进
# ⾏分割再进⾏计算。
#
# content = input("请输入内容:")
# content = content.replace(" ","")  # 5+9
# lst = content.split("+")
# print(int(lst[0]) + int(lst[1]))


# content = input("请输入一个字符串") # faskdjlfjdkas123fasdf4asf1a23sd4f5
# count = 0
# for c in content:
#     if c.isdigit():
#         count += 1
# print(count)


'''
⽤户可持续输⼊（⽤while循环），⽤户使⽤的情况：
输⼊A，则显示⾛⼤路回家，然后在让⽤户进⼀步选择：
是选择公交⻋，还是步⾏？
选择公交⻋，显示10分钟到家，并退出整个程序。
选择步⾏，显示20分钟到家，并退出整个程序。
输⼊B，则显示⾛⼩路回家，并退出整个程序。
输⼊C，则显示绕道回家，然后在让⽤户进⼀步选择：
是选择游戏厅玩会，还是⽹吧？
选择游戏厅，则显示 ‘⼀个半⼩时到家，爸爸在家，拿棍等你。’并让其
重新输⼊A，B,C选项。
选择⽹吧，则显示‘两个⼩时到家，妈妈已做好了战⽃准备。’并让其重
新输⼊A，B,C选项


while 1:
    xuan = input("请选择A,B,C：")
    if xuan.upper() == 'A':
        print("走大路回家")
        traffic = input("请选择公交车还是步行")
        if traffic == '公交车':
            print("10分钟到家")
        else:
            print("20分钟到家")
        break
    elif xuan.upper() == "B":
        print("⾛⼩路回家")
        break
    elif xuan.upper() == 'C':
        print("绕道回家")
        choice = input("请输入你要去游戏厅还是网吧")
        if choice == "网吧":
            print("两个⼩时到家，妈妈已做好了战⽃准备。")
        else:
            print("⼀个半⼩时到家，爸爸在家，拿棍等你。")
    else:
        print("山炮。 回去重新输入~!!!!!!")
'''


# count = 1
# sum = 0
# while count < 100:
#     if count == 88:
#         count += 1
#         continue
#     if count % 2 == 1:
#         sum += count
#     else:
#         sum -= count
#     count += 1
# print(sum)

# s = "西西里的美丽传说"
# count = len(s) - 1  # 最后一个字符的索引
# while count >= 0:
#     # 进行累加
#     print(s[count])
#     count -= 1
