# class Foo:
#     def play(self):
#         print("Foo中的play")
#     def func(self):
#         print("我是爹")
#
# class Foo2:
#     def money(self):
#         print("干爹给钱")
#
#     def play(self):
#         print("Foo2中的play")
#
# class Bar(Foo, Foo2): # 继承   子类,  MRO算法. C3算法
#     pass
#
# obj = Bar()
# # obj.money()
# # obj.func()
# obj.play()

# class Pet:
#     def __init__(self, name):
#         self.name = name
#
#     def chi(self):
#         print("吃,.....")
#     def sleep(self):
#         print("睡")
#
# class Cat(Pet):
#     def catchMouse(self):
#         print("%s喜欢抓老鼠" %  self.name)
#
# class Dog(Pet):
#     def chaijia(self):
#         print("狗会拆家")
#
# class Snake(Pet): # 蛇是一种宠物, x是一种y的时候. x继承y
#     pass
# c = Cat("佩奇")
# c.chi()
# c.sleep()
# c.catchMouse()


# class Car:
#     def run(self):
#         print("车会跑")
#
#
# class BMWCar(Car):
#     pass


# class Animal:
#     def dong(self):
#         pass
#
# class Cat(Animal):
#     def catchMaouse(self):
#         pass
#
#
# # 变量 = 类名()
# c = Cat() # 猫类型的
# c.catchMaouse()
# c.dong()
#
# c = "alex"
# python本来就是多态. 里面没有所谓的类型.

# class Animal:
#     def chi(self):
#         print("所有的动物都会吃")
#
# class Haski(Animal):
#     def chi(self):
#         print("疯了一样的吃")
#
# class Monkey(Animal):
#     def chi(self):
#         print("龇牙咧嘴的吃")
#
# class Tiger(Animal):
#     def chi(self):
#         print("跟猫一样的吃")
#
# class Elphant(Animal):
#     def chi(self):
#         print("大象用鼻子卷着吃")
#
# class YingWu(Animal):
#     def chi(self):
#         print("xxxxx")
#
#
# class SiYangYuan:
#     def wei(self, ani):  # 多态性. 超强的可扩展性. 不论传递进来的是什么. 都统一当成动物来对待.
#         ani.chi()
#
# syy = SiYangYuan()
#
# # 造动物
# hou = Monkey()
# ha = Haski()
# lao = Tiger()
# yw = YingWu()
#
# syy.wei(ha)
# syy.wei(hou)
# syy.wei(lao)
# syy.wei(yw)


class Car:
    def run(self, speed):
        print("车能跑%s迈" % speed)

c = Car() # 实例化一个对象
# Car.run(c, 50)
c.run(50)