class Foo:
    # @staticmethod
    # def __liuwei():
    #     print("你怎么回来了")

    def chi(self):
        print(self)
        print("我很能吃")
        # Foo.__liuwei()

class Bar:
    pass

b = Bar()
Foo.chi(b) # 可以跨类访问. 但是这种写法.逻辑不通.
#
# # Foo.__liuwei()
# f = Foo()
#
# f.chi()
# Foo.chi(f) # f.chi()