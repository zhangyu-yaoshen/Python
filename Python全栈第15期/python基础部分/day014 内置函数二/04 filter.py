# lst = [23, 28, 15, 27, 24, 22]
# def func(age):
#     return age > 18 and age % 2 == 0
#
# f = filter(lambda age: age > 18 and age % 2 == 0, lst)
# # print(sorted(f))
# # f = filter(func, lst)
# # print(f)
# # print("__iter__" in dir(f))
#
# for el in f:
#     print(el)

# lst = [23, 28, 15, 27, 24, 22]
# f = filter(lambda age: age % 2 == 0, filter(lambda age: age > 18, lst))
# print(list(f))

# lst = [{"id":1, "name":'alex', "age":18},
#  {"id":2, "name":'wusir', "age":16},
#  {"id":3, "name":'taibai', "age":17}]
#
# # 筛选出年龄大于等于17岁的人
# print(list(sorted(filter(lambda dic: dic['age'] >= 17, lst), key=lambda dic: dic['age'])))
