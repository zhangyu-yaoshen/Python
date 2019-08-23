import pickle

#  dumps 序列化。 把对象转化成bytes
#  loads 反序列化。 把bytes转化成对象
#  dump 序列化。 把对象转化成bytes并写入文件
#  load 反序列化。把文件中的bytes读取。转化成对象

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def catchMouse(self):
        print(self.name, self.age, "抓老鼠")


# c = Cat("jerry", 18)
# c.catchMouse()


# # dumps 把对象转化成bytes  序列化
# bs = pickle.dumps(c)
# print(bs)
# #
# # 把bytes 转换回对象  反序列化
# ccc = pickle.loads(bs)
# ccc.catchMouse()

# dic = {"jay": "周杰伦", "jj": "大阳哥"}
# bs = pickle.dumps(dic)
# print(bs)
# #
# d = pickle.loads(bs)
# print(d)

# c = Cat("jerry", 18)
# f = open("pickle-test.txt", mode="wb")
# pickle.dump(c, f) # 结果人是看不了的。
#
# f.close()
# f = open("pickle-test.txt", mode="rb")
# c = pickle.load(f)
# c.catchMouse()

lst = [Cat("猫1", 10), Cat("猫2", 9), Cat("猫3", 9), Cat("猫4", 9), Cat("猫5", 9)]

f = open("pickle-test.txt", mode="wb")
pickle.dump(lst, f)
# for el in lst:
#     pickle.dump(el, f)

f.flush()
f.close()
#
f = open("pickle-test.txt", mode="rb")
while 1:
    try:
        c1 = pickle.load(f)
        c1.catchMouse()
    except EOFError:
        break





