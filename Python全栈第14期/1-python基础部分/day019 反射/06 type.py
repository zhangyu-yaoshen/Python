# class Animal:
#     pass
#
# class Cat(Animal):
#     pass
#
# class BoSiCat(Cat):
#     pass
#
# c = Cat()
# print(type(c)) # 比较精准的给出对象的类

# 计算a+b的结果并返回. 两个数相加
def add(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a + b
    else:
        print("算不了")

print(add("胡汉三", 2.5))

