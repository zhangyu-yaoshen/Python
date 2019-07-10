# 写函数，接收n个数字，求这些参数数字的和。（动态传参）
def func(*n):
    sum = 0
    for el in n:
        sum += el
    return sum

ret = func(1,2,5,4,7)


# 写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等),
# 将每个实参的每个元素依次添加到函数的动态参数args里面.
# 例如 传入函数两个参数[1,2,3] (22,33)最终args为(1,2,3,22,33)

# def func(*args): # str, list, tuple, set
#     print(args)
#     # lst = []
#     # for el in args:
#     #     for e in el:
#     #         lst.append(e)
#     # tu = tuple(lst)
#     # print(tu)
#
# func(*"哈哈", *[1,3,5], *(456,789))


# 写函数,传入函数中多个实参(实参均为字典),将每个实参的键值对依次添加到函数的动态参数kwargs里面.
# 例如 传入函数两个参数{‘name’:’alex’} {‘age’:1000}最终kwargs为{‘name’:’alex’ ,‘age’:1000}
# def func(**kwargs):
#     print(kwargs)
#
# func(**{"alex": "大帅逼", "wusir":"丑"})



# 9，写函数,接收一个参数(此参数类型必须是可迭代对象),将可迭代对象的每个元素以’_’相连接,形成新的字符串,并返回.
# 例如 传入的可迭代对象为[1,'老男孩','武sir']返回的结果为’1_老男孩_武sir’
# def func(it):
#     # result = ""
#     # for el in it:
#     #     result += str(el) + "_"
#     # return result[:-1]
#     for i in range(len(it)):
#         el = str(it[i])
#         it[i] = el
#     return "_".join(it)
#
# print(func([1,"alex","wusiar"]))
# print("alex"+213)


# 写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
# 例如:min_max(2,5,7,8,4) 返回:{‘max’:8,’min’:2}(此题用到max(),min()内置函数)

# def func(*n):
#     return {"最大值":max(n), "最小值":min(n)}
#
# print(func(1,8,6,4,5,15,63,35,5))


# 求阶乘
# def func(n):
#     sum = 1
#     for i in range(n, 0, -1):
#         sum *= i
#     return sum
# print(func(5))



# 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
# 例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃’，‘A’)]

# 花色：红黑芳草
# 点数: A2345678910
# 笛卡儿积.
# def func():
#     hua = ["红心", "黑桃", "梅花", "方块"]
#     dian = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#     result = []
#     for huase in hua:
#         for dianshu in dian:
#             result.append((huase, dianshu))
#     return result
#
#
# def wrapper():
#     def inner():
#         print(666)
#
#     return inner # 函数名可以作为变量返回
#
#
# fn = wrapper()
# fn()

# def extendList(val, list=[]): # 默认值在内存中只会产生一份
#     list.append(val)
#     return list
#
# list1 = extendList(10)
# print('list1=%s' % list1)
# list2 = extendList(123, [])
# print('list2=%s' % list2)
# list3 = extendList('a')
# print('list3=%s' % list3)
#
# print(id(list1))
# print(id(list3))
# print(id(list2))


# 写代码完成99乘法表.(升级题)
# 1 * 1 = 1
# 2 * 1 = 2 2 * 2 = 4
# 3 * 1 = 3 3 * 2 = 6 3 * 3 = 9
# ......
# 9 * 1 = 9 9 * 2 = 18 9 * 3 = 27 9 * 4 = 36 9 * 5 = 45 9 * 6 = 54 9 * 7 = 63 9 * 8 = 72 9 * 9 = 81
#
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%s x %s = %s" % (i, j, i*j), end=" ")
#     print() # 换行
#
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
