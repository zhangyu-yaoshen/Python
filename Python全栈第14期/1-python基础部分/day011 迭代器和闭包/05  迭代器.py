# for c in 123:
#     print(c)


# iterable 可迭代的, str, list. tuple, dict, set, open(), range()
# dir() 可以查看某数据类型中可以执行的方法
# s = "alex"
# print(dir(s)) # 在字符串中发现了__iter__. 没有__next__
# a = 123
# print(dir(a)) # 在int中没有__iter__ 没有__next__
# lst = [1, 2, 3,]
# print(dir(lst)) # 在list中也有__iter__

# 所有包含了__iter__的东西都可以使用for循环. 都可以进行迭代
# 迭代器, 在for循环内部. 调用了__iter__(), 访问__iter__()可以得到迭代器
lst = [1, 2, 3, 4, 5, 6]

# it = lst.__iter__()  # iterator 迭代器
# while 1:
#     try:
#         print(it.__next__())
#     except StopIteration:
#         print("结束了")
#         break

for el in lst:
    print(el)
else:
    print("结束了")


# # 迭代器给所有的数据类型提供了一种统一的遍历的方式(可迭代协议), Iterable, __iter__()
# lst = [1, 2, 3, 4, 5]
# print("__iter__" in dir(lst))
# print("__next__" in dir(lst))
#
# it = lst.__iter__()
# # print("__iter__" in dir(it)) #  迭代器里面是有__iter__的.  迭代器一定是可迭代的
# # print("__next__" in dir(it))
#
# for el in it: # 迭代器可以使用for循环
#     print(el)

# 小总结
# Iterable: 可迭代对象. 里面包含了__iter__(),可以使用for循环
# Iterator: 迭代器. 里面包含了__iter__() 和 __next__(), 也可以使用for循环

# from collections import Iterable # 可迭代的
# from collections import Iterator # 迭代器
#
# lst = ["周润发","麻花藤","刘伟"]
# print(isinstance(lst, Iterable)) # instance  实例, 对象
# print(isinstance(lst, Iterator)) # instance  实例, 对象
#
# it = lst.__iter__()
# print(isinstance(it, Iterable)) # instance  实例, 对象
# print(isinstance(it, Iterator)) # instance  实例, 对象

#  总结
#  特点:
#   1. 节省内存
#   2. 惰性机制
#   3. 只能向前. 不能反复

# lst = [1,2,3]
# it = lst.__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
#
# # 重新拿一个迭代器
# it = lst.__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())


