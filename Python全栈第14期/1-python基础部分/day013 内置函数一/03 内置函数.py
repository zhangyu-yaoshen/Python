lst = ["刘伟", "昨天", "没睡觉","干什么去了?"]
# it = lst.__iter__() # 获取迭代器
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# it = iter(lst) # 内部执行的依然是__iter__()
#
# print(it.__next__())
# print(next(it)) # 内部使用的是__next__()

# s = 12378945612345678946
# print(hash(s)) # 计算之后是个数.

# print(help(str))

# def func():
#     pass
# print(callable(func)) # 可以被调用
# print(callable("刘伟"))
# a = 123
# print(callable(a)) # 可以帮我们区分 函数和普通变量


# apple = 3.5
# print(type(apple))  # 浮点型有误差

# a = 5
# print(bin(a)) # 0b

# a = 8
# print(oct(a)) # 0o10

# a = 16
# print(hex(a)) # 0x100000EAB

# print(abs(-1))
# print(divmod(10, 3)) # 返回元组。（商，余数）


# print(round(4.5))  #  不好用. 五舍六入, 四舍五入  4.5浮点数. 4.499999999999999999999  9.500000000000001

# print(pow(2, 10)) # 1024

# sum： 求和
# lst = [1, 2, 3, 4, 5]
# lst2 = [6,7,8,9,10]
# print(sum([0,1,2,3], 0))
# sum(Iterable, start) 把可迭代对象进行循环，计算和。 然后和后面的start做累加。 start默认值是0
# sum(lst, sum(lst2))

# max: 最大值
# print(max(1,3, 4, 6, 12, 1, 5)) # 求最大值

# min: 最小值
# print(min(1, 5, 9 ,-6,18,-6))

# s = {"刘伟", "刘德华", "刘能"}
# ss = frozenset(s)
# dic = {ss:"很6"}
# print(dic)

# list: 可变
# tuple: 不可变的list
#
# set： 可变
# frozenset: 不可变

# lst = ["看不见的房客", "傻瓜", "那个男人来自地球"]
# for el in lst: #  没有索引
#     print(el)

# for i in range(len(lst)): # 可以直接拿到索引
#     print(lst[i]) # 通过索引拿元素

# for index, el in enumerate(lst, 100): # (0, '看不见的房客') 拿到索引和元素
#     print(index, el)

# print(any([False, False, 1, [], {}]))  #  any   or  或者.
# print(all(["马云", True, 1, 188, "麻花藤"]))  # all  and  并且.

# zip
# lst1 = ["中国", "美国", "俄罗斯", "日本"]
# lst2 = ["北京", "华盛顿", "莫斯科"]
# lst3 = ["烤鸭", "炸鸡", "黄油+面包", "寿司"]
#
# a = zip(lst1, lst2, lst3) # 合并列表, 返回可迭代对象, 水桶效应
# print("__iter__" in dir(a))
#
# for el in a:
#     print(el)

# lst = [1, 3, 5, 7, 9]
# # it = reversed(lst)
# # for el in it:
# #     print(el)
#
# # lst[1:3]
# s = slice(1, 3) # 切片
# print(lst[s])
#
# print(lst[1:3])

# 字符串格式化
# print(format("test", "<20"))
# print(format("test", ">20"))
# print(format("test", "^20"))

# 数值
# s = format(7, "b")
# print(type(s))

# print(format(21002, 'c')) # unicode
# print(format(31, 'x'))  # 小写
# print(format(31, 'X'))  # 大写


# print(format(1234567810000000000, 'e')) # 科学记数法 12345678, 默认保留小数点后6位
# print(format(1234567810000000000, '.2e')) # 科学记数法 12345678, 默认保留小数点后2位
# print(format(1234567810000000000, '.8E')) # 科学记数法 12345678, 默认保留小数点后8位

# print(format(0.00001251123456789, 'f')) # 小数点后留6位
# print(format(0.00001251123456789, '.2f')) # 小数点后留2位
# print(format(0.00001251123456789, '.8F')) # 小数点后留8位
#
#
# print(format(1.23456789e+10000, 'F')) # INF infnate


# s = "alex哈哈"
# bs = s.encode("utf-8") # utf-8 兼容ASCII
# print(bs)

# bss = bytes(s, encoding="UTF-8")
# print(bss)

# ret = bytearray('刘伟',encoding='utf-8')  # 周 \x  \x  \x
# print(ret[0], ret[1], ret[2], ret[3], ret[4], ret[5])
# print(ret)

# 没什么用
# s = memoryview("麻花藤".encode("utf-8")) # 看的bytes # 0x00000244E0B85F48
# print("__iter__" in dir(s))


# print(ord("国"))
# print(chr(65))
#
# for i in range(65536):
#     print(chr(i), end=" ")



# print(ascii('a'))
# print(ascii('好')) # '\u597d'不是ascii中的内容


# s = "我叫\\  haha  \周杰伦" #  \应该表示转义  \n \t \r \\
# print(s)
# print(repr(s)) # 把字符串的官方解释给还原回来


# s = "['哈哈', 'hehe', '吼吼']"  # eval可以帮我们还原一些字符串类型的代码  json, list
# res = eval(s)
# print(res)
# print(res[1])

# content = input("请输入你要执行的代码(5+9):")
# res = eval(content)
# print(res)

# exec() # execute 执行, 没有返回值

# exec("for i in range(10): print(i)") # 可以帮我们执行一段代码

# exec('a = 1+2+3') # 一行一行跑
# print(a)
# print(a)  # 眼见不一定为实

# exec 没有返回值

# compile 编译 .


code1 = """
for i in range(10): 
    print(i)
print("刘伟")

def func():
    print("我是函数")
func()
"""
# c = compile(code1, "", "exec")
# exec(c)

# code2 = "1+2+3"
# c = compile(code2, "", "eval")
# res = eval(c)
# print(res)

# code3 = "name = input('请输入你的名字:')"
# c = compile(code3, "", "single")
# exec(c)
# print(name)






