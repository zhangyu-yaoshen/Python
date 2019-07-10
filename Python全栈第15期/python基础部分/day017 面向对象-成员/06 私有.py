class Tiger:

    def __init__(self, name, waibiao, qingzhenglianjiedezuofeng, qingfu, money, fangchan):
        self.name = name
        self.waibiao = waibiao
        self.qingzhenglianjiedezuofeng = qingzhenglianjiedezuofeng
        self.__qingfu = qingfu
        self.__money = money
        self.__fangchan = fangchan

    def buy(self):
        print("我有%s" % self.__money)
        self.__sel()

    def __sel(self):
        print("我要卖掉%s" % self.__fangchan)


lh = Tiger("alex", "正直", "非常刚正不阿, 666", "小潘潘", 10000000000, 5)
print(lh.qingzhenglianjiedezuofeng)
print(lh.name)
print(lh.waibiao)
lh.buy()
# lh.__sel()
# print(lh.__money)