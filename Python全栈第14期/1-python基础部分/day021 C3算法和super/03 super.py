# class Base:
#     def chi(self):
#         print("我没这么干过")
# class Animal(Base):
#     def chi(self):
#         super().chi()
#         print("吃。。。。。。。")
#
# class Cat(Animal,Base): # Cat Animal Base
#     def chi(self): # 覆盖， 重写
#         super().chi() #  可以把父类中被重写了的内容 引入进来.
#         # super(Cat, self).chi() # py2的
#         print("吃鱼")
#
# c = Cat()
# c.chi()


class Foo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Bar(Foo):
    def __init__(self, a, b, c, d):
        super(Bar, self).__init__(a, b, c)
        self.d = d

b = Bar(1,2,3,4)
print(b.__dict__)
#
