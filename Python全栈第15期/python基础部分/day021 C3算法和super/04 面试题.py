# MRO + super ⾯试题
class Init(object):
    def __init__(self, v):
        print("init")
        self.val = v
class Add2(Init):
    def __init__(self, val):
        print("Add2")
        super(Add2, self).__init__(val)
        print(self.val)  # 5
        self.val += 2 # 7
class Mult(Init):
    def __init__(self, val):
        print("Mult")
        super(Mult, self).__init__(val)
        self.val *= 5
class HaHa(Init):
    def __init__(self, val):
        print("哈哈")
        super(HaHa, self).__init__(val)
        self.val /= 5
class Pro(Add2,Mult,HaHa): #
    pass
class Incr(Pro):
    def __init__(self, val):
        super(Incr, self).__init__(val)
        self.val += 1

print(Incr.__mro__)

# p = Incr(5)  # MRO: Incr Pro Add2 Mult HaHa Init
# # 一个对象. p :  val: 8
# print(p.val)
c = Add2(2) # MRO: ADD2 INIT
print(c.val)