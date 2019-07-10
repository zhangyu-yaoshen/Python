# class Base:
#     pass
#
# class Foo(Base):
#     pass
# def func(arg):
#     if isinstance(arg, Base): # 约束这个函数传递进来的对象必须是xxx家族体系下的内容
#         pass
# b = Foo()

'''
可以被调用的
    1. 函数()
    2. 类()   创建对象. 初始化对象  __new__  __init__
    3. 对象()   方法__call__()
    4. 对象.方法()
    变量可以被调用么????
        callable(a)
'''

# def func(arg):
#     if callable(arg): # 判断是会否可以被调用
#         return arg()    # 调用
#     else:
#         print(arg)

# from types import  FunctionType, MethodType
# class Foo:
#     pass
#
# class Person:
#     def chi(self):
#         pass
#
# def func(*args):
#     fun_count = 0
#     method_count = 0
#     foo_object = 0
#     for el in args:
#         if isinstance(el, FunctionType):
#             fun_count += 1
#         elif isinstance(el, MethodType):
#             method_count += 1
#         elif type(el) == Foo:
#             foo_object += 1
#         else:
#             print(el)
#     return fun_count, method_count, foo_object # (元组)
# lst = [Person.chi,  Person().chi, func, Foo()]
# a, b, c = func(*lst)
# print(a, b, c)


# class Foo:
#     def __init__(self):
#         self.name = '小猪'
#         self.age = 100
#         self.name = "alex"
#
#     @property
#     def haha(self):
#         return 10
#
#
# obj = Foo()
# setattr(obj, 'email', 'wupeiqi@xx.com')
# print(obj.__dict__)

# class Foo(object):
#     def __init__(self):
#         self.name = ' '
#         self.age = 100
#
#
# obj = Foo()
# setattr(Foo, 'email', 'wupeiqi@xx.com')
# v1 = getattr(obj, 'email')
# v2 = getattr(Foo, 'email')
# print(v1,v2)

class Perseon:
    # 这个类如果写了__iter__ 这个类的对象就是一个可迭代对象
    # def __iter__(self):
    #     # 准备写一个迭代器
    #     # 生成器就是迭代器
    #     return (i for i in range(10))

    def __call__(self, *args, **kwargs):
        print("刘伟好帅")
obj = Perseon()
obj()
# for el in obj:
#     print(el)

#
# it = obj.__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

