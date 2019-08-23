# # 装大象, 脚本
# print("打开冰箱门")
# print("装大象")
# print("关上冰箱门")
#
# # 函数式编程
# def kaimen():
#     print("打开冰箱门")
# def zhuangdaxiang():
#     print("装大象")
# def guanmen():
#     print("关门")
# kaimen()
# zhuangdaxiang()
# guanmen()


# # 面向对象
# class Elphant:
#
#     def open(self):
#         print("大象会开门")
#     def zhuang(self):
#         print("把自己装进去")
#     def close(self):
#         print("把门关上")
#
# # 创建大象
# e = Elphant()
# e.open()
# e.zhuang()
# e.close()

# 第一回合. 面向过程赢


# 第二回合. 小猪佩奇(name, age, 技能)大战奥特曼, 蜘蛛侠, 蝙蝠侠
# 函数式
# def da_ao_te_man(name, age, jineng):
#     print("%s, %s岁了, 用技能%s 打奥特曼" % (name, age, jineng))
# def da_zhi_zhu_xia(name, age, jineng):
#     print("%s, %s岁了, 用技能%s 打蜘蛛侠" % (name, age, jineng))
# def da_bian_fu_xia(name, age, jineng):
#     print("%s, %s岁了, 用技能%s 打蝙蝠侠" % (name, age, jineng))
#
# da_ao_te_man("小猪佩奇", 40, "嘴巴嘟嘟")
# da_zhi_zhu_xia("小猪佩奇", 40, "嘴巴嘟嘟")
# da_bian_fu_xia("小猪佩奇", 40, "嘴巴嘟嘟")


# 面向对象
class Pig:

    def __init__(self, name, age, jineng):
        self.name = name
        self.age = age
        self.jineng = jineng

    def da_ao_te_man(self):
        print("%s, %s岁了, 用技能%s 打奥特曼" % (self.name, self.age, self.jineng))
    def da_zhi_zhu_xia(self):
        print("%s, %s岁了, 用技能%s 打蜘蛛侠" % (self.name, self.age, self.jineng))
    def da_bian_fu_xia(self):
        print("%s, %s岁了, 用技能%s 打蝙蝠侠" % (self.name, self.age, self.jineng))

peiqi = Pig("小猪佩奇", 40, "嘴巴嘟嘟") # 把这三个属性封装到了一个对象里.
peiqi.da_ao_te_man()
peiqi.da_zhi_zhu_xia()
peiqi.da_bian_fu_xia()


# 平手. 当属性和方法非常多的时候, 才能感觉到面向对象的好.
# 你要知道. 面向对象和面向过程都是思想. 用哪一个取决于业务逻辑.