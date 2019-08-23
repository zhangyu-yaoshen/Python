# lst = ["渣渣辉", "古天绿", "陈小春", "彭佳慧", "郑中基", "胡辣汤"]
# # lst.clear()
# # for el in lst: # for 内部有一个变量来记录当前被循环的位置, 索引.
# #     lst.remove(el) # 直接删除. 是删不干净的. 原因是每次删除都设计到元素的移动. 索引在变.
#
# # 先把要删除的内容保存在一个新列表中. 循环这个新列表. 删除老列表
# new_lst = []
# for el in lst:
#     new_lst.append(el)
# for el in new_lst:
#     lst.remove(el)
# print(lst)

# lst = ["张无忌", "张三丰", "张翠山", "张嘉译", '刘嘉玲', "刘能", '刘老根']
# # 删除姓张的人
# new_lst = []
# for el in lst:
#     if el.startswith("张"):
#         new_lst.append(el)
#
# for el in new_lst:
#     lst.remove(el)
# print(lst)

dic = {"谢逊": '金毛狮王', "韦一笑":"青翼蝠王","殷天正":"白眉鹰王","金花婆婆":"紫衫龙王"}
print(dic)
for k in dic:
    dic['谢逊'] = "张无忌他爹"
print(dic)
