# 1. 新增
# lst = []
# lst.append("周杰伦") # 追加 在最后添加, 效率比较高
# lst.append("周芷若")
# lst.append("周公瑾")
# print(lst)

# lst = ["刘德华", "渣渣辉", "古天乐", "陈小春"]
# lst.insert(2,"马德华")  # 插入, 可能会导致元素移动
# print(lst)

# lst = ["刘昊然", "张一山", "徐峥", "黄渤"]
# lst.extend(["刘能", "赵四", "广坤"])
# print(lst)


# 2. 删除 pop, remove, clear, del
# lst = ["刘能", "广坤", "皮长山", "大脚"]

# lst.pop(2) # 可以指定元素删除(索引)
# print(lst)
# s1 = lst.pop() # 默认弹出最后一个
# print(s1)
# s2 = lst.pop()
# print(s2)
# print(lst)

# lst.remove("广坤")
# lst.remove("大脚")
# print(lst)

# lst = ["语文", "数学", "地理", "历史", "英语", "化学"]

# lst.clear() # 清空

# 可以切片删除
# del lst[2]
# del lst[0]
# del lst[::2]
# print(lst)

# lst = ["功夫", "大话西游", "少林寺", "无间道", "战狼", "战狼2"]
# # lst[2] = "西西里的美丽传说"
# lst[-3] = "新世界"
# lst[1:3] = ["一步之遥"]
# lst[1:5:2] = ["胡辣汤", "烩面"] # 注意如果步长不是1. 那么元素的个数要匹配
# print(lst)

# 列表是一个可迭代对象. 可以使用for循环
# for el in lst:
#     print(el)
