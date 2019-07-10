# def func():
#     a = 10
#     print(a)
# func()
# print(a) # 在外面你是访问不到局部变量的, 局部变量是安全的


# 全局变量可能会被修改, 全局变量是不安全的. 可能会被其他函数所更改
# a = 10
# def func():
#     global a
#     a = 20
#     print(a)
# func()
# print(a)

# 用闭包可以保护我们的变量
# 写法: 在外层函数中声明一个变量. 在内层函数使用或者返回这个变量.
# 这个结构叫闭包
# 1.可以保护我的变量
# 2.可以让一个变量常驻内存

# def outer():
#     a = 10 # 常驻内存
#     def inner():
#         print(a) # 在内部使用的外面的变量
#     return inner # 返回了内部函数
#
#
# # ret是inner的地址. ret就是inner
# ret = outer()
# # ret() # 这里执行inner()
# # print("哈哈")
# # print("哈哈")
# # print("哈哈")
# # ret() # inner的执行时间是不确定的
# # print("哈哈")
# # print("哈哈")
# # print("哈哈")
# # ret() # inner的执行时间是不确定的
#
# # def haha():
# #     pass
# # print(ret.__closure__) # 有东西, 就是闭包. None就不是闭包

# 闭包的应用.保护变量, 常驻内存
from urllib.request import urlopen

def func():
    # 闭包. content会常驻内存
    content = urlopen("http://www.xiaohuar.com/").read()
    def inner():
        return content
    return inner

print("加载中...")
g = func() # 网络请求
print("加载完毕")
print(g())
print(g())
print(g())










