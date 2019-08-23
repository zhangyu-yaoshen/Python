# class Boy:
#     def __init__(self, name, xingge, girlFriend=None):
#         self.name = name
#         self.xingge = xingge
#         self.girlFriend = girlFriend
#
#     def yujian(self, girl):
#         self.girlFriend = girl
#
#     def chi(self):
#         if self.girlFriend:
#             print("随便池! %s 和 %s" % (self.name, self.girlFriend.name))
#         else:
#             print("单身狗， 池什么池？")
#
# class Girl:
#     # def __init__(self, name, boyFriend):
#     def __init__(self, name):
#         self.name = name
#         # self.boyFriend = boyFriend
#     def chi(self):
#         print("%s在吃饭" % self.name)
#
#
# girl = Girl("白骨精")
# alex = Boy("金王", "娘")
# alex.chi()
#
# alex.yujian(girl)
# alex.chi()
#
# # 找到alex的女朋友
# print(alex.girlFriend.name)
# alex.girlFriend.chi()



# 一个对多个.

class School:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.__teach_list = []

    def zhaopin(self, t):
        self.__teach_list.append(t)

    def display(self):
        for el in self.__teach_list:
            print(el.name, el.hobby)




class Teacher:
    def __init__(self, name, gender, salary, hobby, school):
        self.name = name
        self.gender = gender
        self.salary = salary
        self.hobby = hobby

        self.school = school

oldboy_bj = School("北京老男孩", "美丽富饶的沙河", "10086")
oldboy_sh = School("北京老男孩， 上海分校", "上海浦东", "10010")
oldboy_sz = School("北京老男孩， 深圳分校（骑士计划)", "南山区", "10000")


t1 = Teacher("配齐", "男", 200000, "上课", oldboy_bj)
t2 = Teacher("太白", "男", 150000, "开车", oldboy_bj)
t3 = Teacher("Eggon", "男", 123456, "钻研技术", oldboy_sh)
t4 = Teacher("高鑫", "女", 45678, "相夫教子", oldboy_sz)
t5 = Teacher("日天", "男", 666, "看天", oldboy_sz)


# print(t3.school.address) # 找到老师所在的学校的地址

# oldboy_bj.zhaopin(t1)
# oldboy_bj.zhaopin(t2)
# oldboy_bj.display()
oldboy_sh.zhaopin(t3)
oldboy_sz.zhaopin(t4)
oldboy_sz.zhaopin(t5)
oldboy_sz.display()
