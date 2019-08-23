#
# lst = [1, 8, 18, 19, 97, 12, 3]
# # lst.sort() # lst自带的排序功能
# l2 = sorted(lst) # 排序功能
# print(l2)
#        0         2      2      2       0         2        2       2
lst = ["赵瑞鑫", "刘伟", "刘能", "赵四", "王大拿", "于谦",  "范伟", "沈腾"]

# def func(name):
#     return len(name) % 3 # 返回数字

l2 = sorted(lst, key=lambda name: len(name) % 3)
print(l2)












lst = [{"id": 1, "name": 'alex', "age": 18},
    {"id": 2, "name": 'wusir', "age": 16},
    {"id": 3, "name": 'taibai', "age": 17}]
# 按照年龄对学⽣信息进⾏排序
# def func(dic):
#     return dic['age']
# l2 = sorted(lst, key=func) # 流程: 把可迭代对象的每一项传递给函数. 函数返回一个数字. 根据这个数字完成排序
# print(l2)
# l3 = sorted(lst, key=lambda dic: dic['age'])
# l4 = sorted(lst, key=lambda dic: len(dic['name']))
# l4 = sorted(lst, key=lambda dic: ascii(dic['name'][0]))  # ord()
# print(l4)
