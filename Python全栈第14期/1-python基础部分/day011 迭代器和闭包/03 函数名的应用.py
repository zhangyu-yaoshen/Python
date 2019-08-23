# def chi():
#     print("吃月饼")
# print(chi)
# fn = chi # 函数名可以进行赋值
# a = 10
# b = a
# chi()
# fn()
# 函数名可以像变量名一样进行使用


# def func1():
#     print("我是一个单纯的函数")
#
# def func2(abc): # abc接收到的是一个函数的内存地址
#     abc()  # 执行func1, func1()
#     print("我是func2", abc)
#
# # a = "苹果"
#
# func2(func1) # func1是函数的内存地址, 函数名可以像变量一样进行参数的传递


# def outer():
#     def inner():
#         print("我是里面")
#     return inner
#
# outer()() # ()表示的是执行
# ret = outer() # outer得到的结果是inner
# ret() # 执行的是inner函数

# a = "周润发"
# b = "蓝洁瑛"
# c = "春三十娘"
# d = "简直了"
#
# lst = [a, b, c, d]
# for el in lst:
#     print(el)

# def chi():
#     print("吃饭")
# def he():
#     print("喝饮料")
# def du():
#     print("赌是不好的")
# def chou():
#     print("少抽点烟")
#
# lst = [chi, he, du, chou]
# for el in lst:
#     el()

# a = 10
# print(a + 20)

# 错误的
# def a():
#     pass
# print(a + 10)
#
# def panpan():
#     print("我是潘潘. 我喜欢毒丈夫 ")
#
# def xiaoping():
#     print("我是小萍萍. 我喜欢毒丈夫 ")
#
# def xiaohua():
#     print("我是小花花. 我喜欢毒丈夫 ")
#
# def daguanren():
#     print("大官人喜欢xxxx")
#
# def wangpo(nv, nan): # 核心业务逻辑
#     nv()
#     nan()
#
# wangpo(xiaohua, daguanren) # 王婆代理了大官人和潘潘


# def chi():
#     print("我是吃")
#
# a = chi
# haha = a
# hehe = haha
# bilibili= hehe
#
# bilibili()
# print(bilibili.__name__) # 函数名

def play(wanjv1, wanjv2, wanjv3):
    '''
        玩儿函数
        :param wanjv1: 玩具1
        :param wanjv2: 玩具2
        :param wanjv3: 玩具3
        :return: 开心
    '''
    print("我要玩儿荡秋千")
    return "开心"

play("独木桥", "独轮车", "独眼龙")
print(play.__doc__) # 查看函数文档
print(str.join.__doc__)



