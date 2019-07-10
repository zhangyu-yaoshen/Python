# class Base:
#     def login(self):
#         raise NotImplementedError("没有实现login方法") # 专业的写法
#     def kantie(self):
#         raise NotImplementedError("没有实现看帖功能")
# # 张三
# class Normal(Base):
#     def login(self):
#         print("普通人登陆")
#
# # 李四
# class Member(Base):
#     def denglu(self):
#         print("吧务登陆")
#
# # 王五
# class Admin(Base):
#     def login(self):
#         print("管理员登陆")
#
# def login(obj):
#     print("产生验证码")
#     obj.login() # 标准在这里.  必须由login
#     print("进入主页")
#
# # 场景
# n = Normal()
# m = Member()
# a = Admin()
# login(n)
# login(m)
# login(a)
#
# # 重写：子类对父类提供的方法不满意。 重新去定义这个方法

# from abc import ABCMeta, abstractmethod
#
# class Animal(metaclass=ABCMeta): # 在父类中写出metaclass= xxx  抽象类, 类中存在抽象方法， 类一定是抽象类
#
#     @abstractmethod # 抽象方法
#     def chi(self): # 抽象的概念.
#         pass
#     def haha(self):
#         print("娃哈哈")
#
#
# class Cat(Animal): # 子类必须实现父类中的抽象方法.
#     def chi(self):  # 具体的实现
#         print("猫爱吃鱼")
#
# Cat()




from abc import ABCMeta,abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def login(self):pass

# 张三
class Normal(Base):
    def login(self):
        print("普通人登陆")

# 李四
class Member(Base):
    def login(self):
        print("吧务登陆")

# 王五
class Admin(Base):
    def login(self):
        print("管理员登陆")

def login(obj):
    print("产生验证码")
    obj.login() # 标准在这里.  必须由login
    print("进入主页")

# 场景
n = Normal()
m = Member()
a = Admin()
login(n)
login(m)
login(a)