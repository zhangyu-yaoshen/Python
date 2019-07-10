'''
class HaoHan: # 驼峰. 类名首字母大写.
    def __init__(self, name, waihao, jineng):
        self.name = name
        self.waihao = waihao
        self.jineng = jineng

    def ganLaoHu(self):
        print("%s, %s 在干老虎" % (self.waihao, self.name))

    def shaSaoZi(self):
        print("%s, %s 在杀嫂子" % (self.waihao, self.name))

    def tiTianXingDao(self):
        print("%s, %s 在替天行道" % (self.waihao, self.name))

wusong = HaoHan("武松", "行者", "喝酒")

wusong.ganLaoHu()
wusong.shaSaoZi()
wusong.tiTianXingDao()
'''

'''
class HeShang:

    def __init__(self, fahao, mingzi, age, miao):
        self.fahao = fahao
        self.mingzi = mingzi
        self.age = age
        self.miao = miao

    def nianjing(self):
        print("%s在念经" %  self.fahao)

    def quxifu(self, xifu):
        print("%s取了个媳妇:%s" % (self.fahao, xifu))

hs = HeShang("秃驴", "alex", 38, "路飞庙")
hs.nianjing()
hs.quxifu("wusir")

'''

# class Account:
#
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#     def login(self):
#         if self.username == "alex" and self.password == '123':
#             return True
#         else:
#             return False
#
# acc = Account("alex", "1234")
# print(acc.login())

