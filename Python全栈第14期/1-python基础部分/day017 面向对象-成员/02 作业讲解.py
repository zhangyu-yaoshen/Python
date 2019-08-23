# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def zhouchang(self):
#         return 2 * 3.14 * self.r
#
#     def mianji(self):
#         return 3.14 * self.r * self.r
#
#
# c = Circle(5)
# print(c.zhouchang())

# class Base1:
#     def f1(self):
#         print('base1,1')
#     def f2(self):
#         print('base1,f2')
#     def f3(self):
#         print('base2.f3')
#         self.f1()
#
# class Base2:
#     def f1(self):
#         print('base2,f1')
#
# class Foo(Base1, Base2):
#
#     def f0(self):
#         print("foo.f0")
#         self.f3()
#
# f = Foo()
# f.f0()

# class User:
#     def __init__(self, username, password, email):
#         self.username = username
#         self.password = password
#         self.email = email
#
#
# user_list = []
# for i in range(3):
#     user = input("请输入用户名:")
#     pwd = input("请输入密码:")
#     email = input("请输入邮箱:")
#     u = User(user, pwd, email)
#     user_list.append(u)
# else:
#     for u in user_list:
#         print("我叫%s, 邮箱是:%s" % (u.username, u.email))
#
#


class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


class Account:
    def __init__(self):
        self.user_list = [] # 数据源

    def login(self):
        print("欢迎来到登录环节")
        username = input("请输入用户名: ")
        password = input("请输入密码:")
        for u in self.user_list:
            if u.name == username and u.pwd == password:
                print("登录成功")
                return
        else:
            print("登录失败")

    def register(self):
        print("欢迎来到注册环节")
        uname = input("请输入用户名")
        pwd = input("请输入密码")

        u = User(uname, pwd)
        self.user_list.append(u)

    def run(self):
        while 1:
            print("1. 注册")
            print("2. 登录")
            num = input("请输入你要执行的操作(Q退出):")
            if num == "1":
                self.register()
            elif num == "2":
                self.login()
            elif num.upper() == "Q":
                print("退出")
                break
            else:
                print("你是不是傻")


obj = Account()
obj.run()





