# def func1():
#     print("我是func1")
#
# def func2():
#     print("我是func2")
#     func1()
#
# def func3():
#     func2()
#     print("我是func3")
# func3()
# 这样的代码不是嵌套. 互相调用

# 函数可以互相嵌套
# def outer():
#     def inner():
#         print("我是内部")
#     print("我是外部")
#     inner()
# outer()

# def outer():
#     print("我是外面的")
#     def inner_1():
#         def inner_2():
#             print("我是里面的2")
#         inner_2()
#         print("我是里面的1")
#     inner_1()
#     print("我是外面的收尾")
# outer()

# a = 10
# def func():
#     global a #表示在当前作用域中的使用的a是全局中的变量
#     a = 20 # 所有的a都是外面的了
#     print(a) # 现在只有看的权利
#
# print(a) # 10
# func() # 20
# print(a) # 20
#
#
# def outer():
#     a = 10
#     def inner():
#         nonlocal a # 找的是局部当中, 离他最近的上层的那个变量
#         a = 20
#         print(a)
#     print(a) # 10
#     inner() # 20
#     print(a) # 20
# outer()



a = 1
def fun_1():
    a = 2
    def fun_2():
        nonlocal a
        a = 3
        def fun_3():
            a = 4
            print(a)
        print(a)
        fun_3()
        print(a)
    print(a)
    fun_2()
    print(a)
print(a)
fun_1()
print(a)

# global 引入全局变量, 可以定义全局变量
# nonlocal 引入局部中离他最近的外层变量

# def func():
#     global a # 没有也得有. 自动帮你创建
#     a = 20
#
# func()
# print(a)
