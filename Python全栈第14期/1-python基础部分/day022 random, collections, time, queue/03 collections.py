
# 计算字符串中每个字符出现的次数
# s = "abcdefadsfasfasdfbadsfasdbfdasfdas" # 可迭代
# # dic = {}
# # for c in s:
# #     dic[c] = dic.get(c, 0) + 1
# # print(dic)
#
# from collections import Counter # 引入模块, 计数器
# c = Counter(s)  # 创来和字典差不多
# print(c)
# #
# # lst = ["周杰伦", '周杰伦', "王力宏", "大阳哥", "大阳哥", "刘伟", "刘伟"]
# # c = Counter(lst)
# # print(c)建一个Counter对象
# # print(c)
# # print(c['s']) # 用起
#
# from collections import deque
# d = deque()  # 创建双向队列
# d.append("李茶的姑妈") # 默认在右侧添加
# d.append("无双")
# d.append("影")
# d.append("找到你")
# #让悲伤逆流成河, 理查的姑妈, 无双, 影, 找到你
# print(d)
# d.appendleft("让悲伤逆流成河") # 左侧添加
# print(d)
# print(d.pop()) # 从右边删除
# print(d.pop()) # 从右边删除
# print(d.popleft()) # 从左边删除
# print(d.pop()) # 从右边删除
# print(d)


# from collections import namedtuple
#
# po = namedtuple("Point", ["x", "y"]) # 定义了简单的类-lambda
# p = po(1, 2) # 命名元组
# print(p)

# class Point:
#     def __init__(self,x, y):
#         self.x = x
#         self.y = y
# p = Point(1, 2)

# py3.6以上使用的是新算法. 来自于pypy. 节约20-30%内存
# d = {"a":1,"b":2,"c":3}
# print(d)

# from collections import OrderedDict
# od = OrderedDict({"a":1,"b":2,"c":3})
# print(od.get("b"))
# print(od["b"])


from collections import defaultdict
# d = defaultdict(list) # {} list() 必须是callable
# d['刘伟'] = "奥特曼"
# print(d['大阳哥']) # 当key不存在的时候. 返回默认值.其实就是callable()
# print(d['刘伟'])
#
# # 11 22 33 44 55 66 77 88 99
# lst = [11, 22, 33, 44, 55, 66, 77, 88, 99]
# dic = {}
# for el in lst:
#     if el > 66:
#         dic.setdefault("key1", []).append(el)
#     else:
#         dic.setdefault("key2", []).append(el)
# print(dic)

lst = [11, 22, 33, 44, 55, 66, 77, 88, 99]
dd = defaultdict(list)
for el in lst:
    if el > 66:
        dd['key1'].append(el)
    else:
        dd['key2'].append(el)
print(dd)





