
# while 1:
#     print("拿出手机")
#     print("打开陌陌")
#     print("找一找心怡的对方.")
#     print("出来吃吃饭")
#     print("唱唱歌")
#     print("跳跳广场舞")
#
# print("吃饭")

# 函数是对功能或者动作的封装
# 函数的定义:
# def yue():
#     print("拿出手机")
#     print("打开陌陌")
#     print("找一找心怡的对方.")
#     print("出来吃吃饭")
#     print("唱唱歌")
#     print("跳跳广场舞")
#
# # 函数的调用:  函数名()
# yue()
# print("回家休息休息")
# yue() # 动作就可以在任何时候， 在任何位置， 进行访问

# 当函数执行之后。可以给调用者一个返回值
# def yue(): # 参数
#     print("拿出手机")
#     print("打开陌陌")
#     print("找一找心怡的对方.")
#     print("出来吃吃饭")
#     print("唱唱歌")
#     print("跳跳广场舞")
#     return "小姐姐", "小护士", "广场舞大妈"
#     # return "小姐姐"  # return表示返回。 这个函数在调用之后会得到一个结果
# ret = yue() # 当函数有返回值的时候。 我们可以不接受返回值
# print(ret)

# 在函数中如果不写return 表示函数没有返回值。调用方接收到的是None
# return 可以终止一个函数的运行
# 在函数中写了return。 但是return后面不跟值， 表示函数没有返回值。 接受的是None。
# 在函数中写return。 return后面跟一个值
# 在函数中写return。 return 后面可以跟上多个值, 表示返回多个值。 接收方收到的是元组


# # 形参
# def yue(tools): # 在函数声明的位置。 给出来的参数叫形参。 形式上的一个参数. 用一个变量来表是
#     print("拿出手机")
#     print("打开%s" % tools)
#     print("找一找心怡的对方.")
#     print("出来吃吃饭")
#     print("唱唱歌")
#     print("跳跳广场舞")
#
# # 实参
# # 在函数调用的时候。把实参的值赋值给形参的过程叫传参
# yue("微信") # 在函数调用的地方给出的具体的值。 参数叫实参. 实际参数
# yue("陌陌")
# yue("探探")


# def chi(good_food, no_good_food, drink):
#     print("我要吃",good_food, no_good_food, drink)
#
# # chi("大米饭", "冰峰", "炸鸡")
# # chi(drink="哇哈哈", no_good_food="薯条", good_food="盖浇饭")
# chi("小米饭", "辣条", drink="可乐")
# chi(drink="可乐", "小米饭", "辣条")


def regist(name,sex="男", age=18): # 语法上不允许
    print(name, age, sex)

regist("刘伟", 22)
regist("李铁帅", 27)
regist("高晓燕", 18, "女")
regist("李铁帅", 27)
regist("李铁帅", 27)
regist("李铁帅", 27)
regist("李铁帅", 27)
regist("李铁帅", 27)


# 实参的分类:
# 1. 位置参数. 按照位置。 给形参赋值
# 2. 关键字参数. 按照形参的名字给参数赋值
# 3. 混合参数, 位置参数必须放在前面。 关键字参数放后面

# 形参的分类(3大类)
# 1. 位置参数 按照位置来声明形参
# 2. 默认值参数, 当给参数传递值的时候。 默认值不起作用, 不给值。 默认值起作用. 保证你至少有个值能用
# 顺序: 位置参数必须放在前面。 默认值参数必须放在后面


# 函数：对功能或者动作的封装
# 登陆验证
# def login(username, password):
#     if username == 'alex' and password == "123":
#         return True
#     else:
#         return False
#
# # 使用场景
# name = input("请输入你的账号:")
# pws = input("请输入你的密码:")
# if login(name, pws):
#     print("进入刘伟的空间")
# else:
#     print("用户名或密码错误， 请重新登陆!")

# f(x) = x + 1
# f(3) = 3 + 1 = 4
# def f(x):
#     return x + 1
# print(f(2))
#
# s = "你好啊我叫塞利亚"
# print(len(s))
#
# def my_len(s):
#     count = 0
#     for el in s:
#         count+=1
#     return count
# print(my_len(s))
