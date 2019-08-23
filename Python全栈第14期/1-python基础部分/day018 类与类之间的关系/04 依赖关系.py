class Elephant:

    def __init__(self, name):
        self.name = name


    def open(self, ref): # 想要的是一个冰箱。 是哪个冰箱没有制定
        print("冰箱哥哥， 开门把")
        ref.open_door()

    def close(self, ref): # 依赖关系
        print("冰箱哥哥， 我进来了。 关门把")
        ref.close_door()

    def jin(self):
        print("进冰箱装自己")

class Refrigerator:

    def open_door(self):
        print("冰箱陌陌的打开了自己的门")
    def close_door(self):
        print("冰箱陌陌的关上了自己的门 ")

# class GaoYaGuo:
#     def open_door(self):
#         print("冰箱陌陌的打开了自己的门")
#     def close_door(self):
#         print("冰箱陌陌的关上了自己的门 ")


alex = Elephant("李杰")
bx1 = Refrigerator()

#
alex.open(bx1)
alex.jin()
alex.close(bx1)
object