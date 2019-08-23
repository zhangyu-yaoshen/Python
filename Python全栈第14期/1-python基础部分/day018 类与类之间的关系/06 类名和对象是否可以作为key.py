# 可哈希. 内部是否哈希算法 __hash__

# class Foo(object): # 所有的类都会默认继承object
#     def __init__(self):
#         pass
#     def func(self):
#         pass
#     # __hash__ = None
#
# dic = {}
# dic[Foo] = "123456" # 类名是可哈希的。
# dic[Foo()] = "刘伟" # 类中是否包含__hash__
# print(dic)

# 默认的类和对象都是可哈希的

# class Base:
#     def __init__(self, num):
#         self.num = num
#
#     def func1(self):
#         print(self.num)
#
# class Foo(Base):
#     pass
#
# obj = Foo(123)
# obj.func1() # 123

# class Base:
#     def __init__(self, num):
#         self.num = num
#     def func1(self):
#         print(self.num)
#
# class Foo(Base):
#     def func1(self):
#         print("Foo. func1", self.num)
#
# obj = Foo(123)
# obj.func1() # ???? Foo. func1 123

#
# class Base:
#     def __init__(self, num):
#         self.num = num
#     def func1(self):
#         print(self.num)
#         self.func2()
#     def func2(self):
#         print("Base.func2")
#
# class Foo(Base):
#     def func2(self):
#         print("Foo.func2")
#
# obj = Foo(123)
# obj.func1() # 123

# class Base:
#     def __init__(self, num):
#         self.num = num
#
#     def func1(self):
#         print(self.num)
#         self.func2()
#
#     def func2(self):
#         print(111, self.num)
#
# class Foo(Base):
#     def func2(self):
#         print(222, self.num)
#
# lst = [Base(1), Base(2), Foo(3)]
# for obj in lst:
#     obj.func2()

class Base:
    def __init__(self, num):
        self.num = num

    def func1(self):
        print(self.num)
        self.func2()

    def func2(self):
        print(111, self.num)

class Foo(Base):
    def func2(self):
        print(222, self.num)

lst = [Base(1), Base(2), Foo(3)]
for obj in lst:
    obj.func1()

# 1
# 111 1
# 2
# 111 2
# 3
# 222 3

# 总结： self当前访问xx方法的那个对象


