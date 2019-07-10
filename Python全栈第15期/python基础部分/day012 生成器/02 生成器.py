
# def func():
#     lst = []
#     for i in range(10000):
#         lst.append("衣服%s" % i)
#     return lst
# lst = func()
# print(lst)

# def func():
#     for i in range(1, 10000):
#         yield "衣服%s" % i
#
# gen = func()
# for i in range(50):
#     yf = gen.__next__()
# for i in range(50):
#     yf = gen.__next__()
# for i in range(50):
#     yf = gen.__next__()

# def func():
#     lst = []
#     for i in range(1, 10000):
#         lst.append("衣服%s" % i)
#         if i % 50 == 0:
#             yield lst
#             lst = [] # 新的装衣服的地方
#
# gen = func()
# yf1 = gen.__next__()
# print(yf1)
# yf2 = gen.__next__()
# print(yf2)
# yf3 = gen.__next__()
# print(yf3)
# yf4 = gen.__next__()
# yf5 = gen.__next__()
# print(yf1)
# print(yf2)
# print(yf3)
# print(yf4)
# print(yf5)



# 生成器:本质是迭代器, 写法和迭代器不一样. 用法和迭代器一样
# 生成器函数: 函数中带有yield, 执行生成器函数的时候返回生成器。而不是执行这个函数
# def func():
#     print("你好啊, 我叫赛利亚,")
#     yield "西岚的武士刀" # return 和yield都可以返回数据
#
# ret = func() # generator ret是一个生成器
# print(ret)
# s = ret.__next__() # 当执行到__next__()的时候， 函数才真正的开始执行
# print("接受到的是", s)

# def func():
#     print("打开手机")
#     print("打开陌陌")
#     yield "手机"
#     print("约妹子")
#     print("出来喝喝茶")
#     yield "电脑"
#     print("我加了一句话")
# gen = func() # 生成器
# ret1 = gen.__next__()
# print(ret1)
# ret2 = gen.__next__()
# print(ret2)
# ret3 = gen.__next__()  # 找不到最后一个yield 会报错
# print(ret3)
#

# 特点：
#   1. 节省内存, 几乎不占用内存
#   2. 惰性机制
#   3。只能往前走


# send() 也可以实现类似__next__()的效果, send（）可以给上一个yield传值
#
# def func():
#     print("韭菜盒子")
#     a = yield "哇哈哈"
#     print("肉包子", a)
#     b = yield "脉动"
#     print("锅包肉", b)
#     yield "冰红茶"
#
# gen = func()
# ret = gen.send("胡辣汤")
# print(ret)
#
# ret = gen.send("刘伟") # 给上一个yield传值
# print(ret)
#
# ret = gen.send("刘德华") # 给上一个yield传值
# print(ret)

#  send()和__next__()的区别
# send不可以用在开头
# send可以给上一个yield传值, 不能给最后一个yield传值

def func():
    yield "麻花藤"
    yield "李彦宏"
    yield "马云"
    yield "刘强东"

gen = func()
# print(gen.__next__()) # 麻花藤
# print(gen.__next__()) # 麻花藤
# print(gen.__next__()) # 麻花藤
# print(gen.__next__()) # 麻花藤

# 生成器的本质是迭代器.
# print("__iter__" in dir(gen))
#
# # 生成器可以直接使用for循环
# # for el in gen:
# #     print(el)
#
# lst = list(gen) # 把生成器中的每一个数据拿出来组合成一个列表
# print(lst)












