# 列表：装python1期， python2期。。。。。。
# lst = [] # 创建列表
# for i in range(1, 17): #  循环1-16
#     lst.append("python%s" % i) # 装数据
# print(lst)

# 推导式
# 列表推导式 : [结果 for循环 if筛选]
lst = ["python%s" % i for i in range(1, 17)]
print(lst)

# 创建列表: [1,3,5,7,9..99]
lst = [i for i in range(1, 100, 2)]
print(lst)

lst = [i for i in range(1,100) if i % 2 == 1]
print(lst)


# 获取1-100内能被3整除的数
# lst = [i for i in range(1, 101) if i % 3 == 0]
#
# # 100以内能被3整除的数的平⽅
# lst = [i*i for i in range(1, 101) if i % 3 == 0]
# 寻找名字中带有两个e的⼈的名字

# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven','Joe'],
#  ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
#
# lst = [name for first in names for name in first if name.count("e") >= 2 ]
# print(lst)

# 字典推导式, {key: value for循环 if 筛选}
# dic = {"张无忌":"九阳神功", "乔峰":"降龙十八掌", "楚留香":"帅"}
# d = {dic[k]: k for k in dic}
# print(d)

# lst1 = ["东北", "陕西", "山西", "开封", "杭州", "广东", "济南"]
# lst2 = ['大拉皮', "油泼面", "老陈醋", "灌汤包", "西湖鲤鱼", "早茶", "胶东一锅鲜"]
#
# dic = {lst1[i]:lst2[i] for i in range(len(lst1))}
# print(dic)

# 集合推导式 无序不重复 可哈希
# {key for if}

# lst = ["周杰伦","周伯通","周润发","周伯通","周笔畅","周伯通","周星驰","周伯通"]
# s = {el for el in lst}
# print(s)






