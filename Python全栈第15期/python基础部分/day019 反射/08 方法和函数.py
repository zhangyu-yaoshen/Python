
def func():
    print("我是func")

print(func) # <function func at 0x00000253260678C8>

class Foo:
    # 实例方法: 对象.方法  方法    类名.方法  函数
    def chi(self):
        print("我是吃")

    @staticmethod # 都是函数
    def static_method():
        pass

    @classmethod # 都是方法
    def class_method(cls): # 类对象的内容
        pass
    @property # 神马都不是. 变量
    def age(self):
        return 10

# 引入两个模块
from types import FunctionType, MethodType

def haha(arg):
    print(isinstance(arg, FunctionType)) # False
    print(isinstance(arg, MethodType)) # True
haha(Foo.age)


# f = Foo()
# print(f.chi) # <bound method Foo.chi of <__main__.Foo object at 0x0000022D69C48390>>
# Foo.chi(f)
# print(Foo.chi) # <function Foo.chi at 0x000001A4BBEE79D8>
#
# print(f.static_method) # <function Foo.static_method at 0x000002BBD2DB7A60>
# print(Foo.static_method) # <function Foo.static_method at 0x00000233E2247A60>
#
# print(f.class_method) # <bound method Foo.class_method of <class '__main__.Foo'>>
# print(Foo.class_method) # <bound method Foo.class_method of <class '__main__.Foo'>>
