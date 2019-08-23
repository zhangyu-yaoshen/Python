class Person:

    def __init__(self):
        pass
    # 实例方法需要传递类的对象 self
    def think(self):
        print("人能思考")

    # 静态方法不需要传递对象或者类
    @staticmethod # 静态方法
    def jisuan(a, b):
        print("我来过这里")
        return a + b

    # 类方法: 第一个参数传递的是类名
    @classmethod
    def clsMethod(cls): # cls表示的类
        p = cls() # 可以动态的创建对象.
        print("我是一个类方法", p)


# p = Person()
# p.think()
#
# Person.think(p)

# # 静态方法的调用：
# c = Person.jisuan(1, 2) #  类名可以访问
# print(c)
# #
# p = Person()
# d = p.jisuan(3, 5) # 用对象也可以访问
# print(d)
# # 记住, 静态的内容用类名访问

Person.clsMethod() # 类方法默认第一个参数接收的是类名
