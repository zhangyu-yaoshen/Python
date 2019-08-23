
# # 程序运行过程中产生的错误, 不正常
# def chufa(a, b):
#    try: # 尝试执行xxx代码
#        ret = a/b # 如果这里出现了错误. 异常. 系统内部会产生一个异常对象. 系统会把这个错误抛出. 抛给调用方
#        return ret
#    except ZeroDivisionError as e: # 内部产生的所有异常都会被捕获, 捕获的异常对象会交给e
#        print(e)
#        print("出错了. 0不能是除数")
#    except FileNotFoundError as e:  # 内部产生的所有异常都会被捕获, 捕获的异常对象会交给e
#        print(e)
#        print("出错了. 0不能是除数")
#    except StopIteration as e:  # 内部产生的所有异常都会被捕获, 捕获的异常对象会交给e
#        print(e)
#        print("出错了. 0不能是除数")
#    except Exception as e:  # 内部产生的所有异常都会被捕获, 捕获的异常对象会交给e
#        print(e)
#        print("出错了. 0不能是除数")
#
# ret = chufa(10, 0)
# print(ret)


# 计算两个整数的加法
# def add(a, b):
#     if type(a)!=int or type(b) != int:
#         # return
#         raise TypeError("我这里只要int, 不要别的类型")
#     return a + b
#
# add(123, "abc")

import traceback
class GenderError(Exception):
    pass
class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
def nan_gu_ke_xi_zao(per):
    if per.gender != "男":
        raise GenderError("这里是刘伟的男澡堂子. ")
    else:
        pass
p1 = Person("alex", "不详")
# nan_gu_ke_xi_zao(p1)
p2 = Person("wusir", "不详")
try:
    nan_gu_ke_xi_zao(p2)
except GenderError as g:
    print(g)
    val = traceback.format_exc() # 获取错误堆栈
    print(val)
