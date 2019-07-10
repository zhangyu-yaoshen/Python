import master

# while 1:
#     print("""大牛写了很多的功能:
#     chi
#     he
#     la
#     shui
# """)
#     val = input("请输入你要测试的功能") # he
#
#     if hasattr(master, val):
#         attr = getattr(master, val) # 从xxx对象或者模块中找xxxxx(字符串) 功能, 变量
#         if callable(attr): # 判断这个鬼东西是否可以被调用
#             attr()
#         else:
#             print(attr)
#     else:
#         print("没有这个功能")
#
#     # master.val()
#     #
#     # master."chi"()
#
#
#     # if val == 'chi':
#     #     master.chi()
#     # elif val == "he":
#     #     master.he()
#     # elif val == "la":
#     #     master.la()
#     # elif val == "shui":
#     #     master.shui()
#     # else:
#     #     print("滚犊子")
#

# 把chi函数换成lambda
# print(master.chi)
# setattr(master, "chi", lambda x: x + 1)
# print(master.chi)

delattr(master, "la") # 删除xxx
master.la()

