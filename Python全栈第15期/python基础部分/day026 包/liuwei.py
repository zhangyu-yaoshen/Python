
__all__ = ["money", "chi"] # 此时如果有人导入这个模块. 并且是from xxx import *
money = 5000

def chi():
    print("刘伟喜欢吃东西")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): # 当执行print(对象)
        return self.name + str(self.age)+"明天换套衣服"

