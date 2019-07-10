# def chi(*food): # * 表示的是不定参数. 可以传递任意个信息 参数名是food, 接受到的是元组
#     print("我要吃", food)
#
# chi("一锅大米饭", "一箱辣条", "一桶方便面", "4L可乐")
# chi("方便面")
# chi("一大锅米饭", "一小锅小米饭", "一箱辣条", "一桶方便面", "4L可乐")

# * 表接收位置参数的动态传参
# 传参的顺序
# 位置 *args 默认值 **kwargs
#
# 如果默认值参数在*args前面. 如果想让默认值生效. *args将永远接不到值
# def func( a, b, *args,c = 5): # arguments参数
#     print(a, b, c, args)
#
# func(1,2,3,4,5,6,8,c = 10)

# 关键字的动态传参
# *args 位置参数 接收到的是元组
# **kwargs 关键字的动态传参, 接收到的是字典
# def func(**kwargs): # key word arguments
#     print(kwargs)
#
# func(a=10, b=20, jay="周杰伦", jj="林俊杰")

# 无敌模式. 所有的参数都能接收
# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# func(1, 2, 5, jj="陶喆", jay="zhoujielun", soup="胡辣汤")

# def func(*args): # 在这里. 其实相当于把传进来的参数做了一次聚合, 聚合成一个元组
#     print(args)
#
# lst = "娃哈哈"
# func(*lst) #  在实参位置 * 表示打散, 打散的是可迭代对象


# def func(**kwargs): # ** 把接收到的关键字参数打包(聚合)成字典
#     print(kwargs) # 一定是字典
#
# dic = {"张无忌": "明教教主", "谢逊": "金毛狮王", "范瑶": "光明右使"}
#
# # func(张无忌=dic['张无忌'], 谢逊=dic['谢逊'], 范瑶=dic['范瑶'])
# func(**dic) # 这里的** 是把字典打散. 字典的key作为参数的名字, 字典的值作为参数的值传递给形参

# 在形参上
#   1. 位置参数
#   2. 默认值参数
#   3. 动态参数
#       1. *args  位置参数的动态传参. 系统会自动的把所有的位置参数聚合成元组
#       2. **kwargs  关键字的动态传参. 系统会自动把所有的关键字参数聚合成字典
#       3.  def func(*args, **kwargs): 无敌传参
#       4. 顺序:  位置参数, *args, 默认值, **kwargs
#       5. 在使用的时候, 可以任意的进行搭配
#   4. 在实参上. *, **表示的打散.  在形参. *,** 表示聚合
