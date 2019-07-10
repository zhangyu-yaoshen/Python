# 来一堆数据
# lst = ["python%s期" % i for i in range(505)]
# # print(lst)
#
# # 每页显示xx条数据
# pageSize = 10
# current = int(input("请输入当前页码："))
# # 页数
# totle = 0
# if len(lst)%pageSize == 0:
#     totle = len(lst)//pageSize
# else:
#     totle = len(lst) // pageSize + 1
#
# if current > totle :
#     print("没有数据了。")
# else:
#     # 第一页数据
#     # data = lst[pageSize*0:pageSize]
#     # 第二页
#     data = lst[pageSize*(current-1) : pageSize*current]
#     for d in data:
#         print(d)


class Pager:

    def __init__(self, lst, pageSize):
        self.lst = lst
        self.pageSize = pageSize

    def start(self): # 1
        return self.__zhiding(1)

    def end(self): # 最后一页
        return self.__zhiding(self.totle)

    def index(self): # 指定某一页
        page = int(input("请输入你要显示的页码:"))
        return self.__zhiding(page)

    def __zhiding(self, page):
        return self.lst[self.pageSize * (page - 1): self.pageSize * page]

    @property
    def totle(self):
        totle = 0
        if len(self.lst)%self.pageSize == 0:
            totle = len(self.lst)//self.pageSize
        else:
            totle = len(self.lst) // self.pageSize + 1
        return totle


p = Pager([i for i in range(20000)], 100)
print(p.end())
print(p.index())


