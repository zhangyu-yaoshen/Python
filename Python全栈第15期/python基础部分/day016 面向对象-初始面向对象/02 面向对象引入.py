# 定义一辆车
class Car:
    # 出厂设置.(__init__) 构造方法
    def __init__(self, color, pai, pailiang, own): # self 表示当前类的对象
        # print("我在造车")
        # print(self)
        # 绑定属性.
        self.color = color
        self.pai = pai
        self.pailiang = pailiang
        self.own = own

    # 车能跑. 跑是一个动作. 要写函数(方法)
    def run(self):  # self: 当前类的对象
        print("%s颜色的车在疯狂的跑" % self.color)  # self就是你当前正在执行这个动作的对象.
        print(self)

    def tiaogao(self):
        print("有一台%s色的车在疯狂跳高" %  self.color)

c1 = Car("红", "京A66666", "2.0T", "alex") # 自动的调用__init__函数(方法)
c1.run() # 对象.方法()
c1.tiaogao()
print(c1)
# print(c1.__dict__)
# c1.color = "绿色"
# 字典.
# print(c1.color)
c2 = Car("黑色", "京B22222", "1.5L", "小猪佩奇") # 没有参数
c2.run()
print(c2)
# print(c2.color) # ????






# # 创造一辆车
# c = Car()  # 类名()
#
# c.color = "黑色"  # 对象.属性
# c.pai = "京A66666"
# c.pailiang = "2.0t"
# c.own = "alex"
# print(c.pai)
#
# c1 = Car()  # 创建新对象. 又叫做实例化  # 类是一个概念. 对象:具体的实例
# c1.color = "白色"
# c1.pai = "京B22222"
# c1.pailiang = "1.6T"
# c1.own = "小猪佩奇"
# print(id(c), id(c1))
# print(c1.pai)
# print(c.own)

# print(type(c))
