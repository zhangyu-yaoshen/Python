#!/usr/bin/env python
# -*- coding:utf-8 -*-
##################################【dict字典】########################################
# 1、清空
# zhangyu_dict = {
#     "姓名":"张禹",
#     "性别":"男",
#     "年龄":"29",
# }
# zhangyu_dict.clear()#清空字典
# print(zhangyu_dict)
# 2、浅拷贝
# zhangyu_dict = {
#     "姓名":"张禹",
#     "性别":"男",
#     "年龄":"29",
# }
# v = zhangyu_dict.copy()
# print(v)
# print(zhangyu_dict)
# 3、获取【根据KEY获取指定的value；不存在不报错】
# zhangyu_dict = {
#     "姓名":"张禹",
#     "性别":"男",
#     "年龄":"29",
# }
# v = zhangyu_dict.get("姓名")
# print(v)
# 4、删除并获取对应的value值
# zhangyu_dict = {
#     "姓名":"张禹",
#     "性别":"男",
#     "年龄":"29",
# }
# v = zhangyu_dict.pop("姓名")
# print(v)
# print(zhangyu_dict)
# 5、随机删除一个键值对；并且获取到删除的键值
# zhangyu_dict = {
#     "姓名":"张禹",
#     "性别":"男",
#     "年龄":"29",
# }
# k,v = zhangyu_dict.popitem()
# print(k,v)
# print(zhangyu_dict)
# 6、增加；如果存在则不做操作
# zhangyu_dict = {
#     "姓名":"张禹",
#     "性别":"男",
#     "年龄":"29",
# }
# zhangyu_dict.setdefault("K1","999")
# print(zhangyu_dict)
# 7、批量增加或修改
zhangyu_dict = {
    "姓名":"张禹",
    "性别":"男",
    "年龄":"29",
}
zhangyu_dict.update({"a1":"111"})
print(zhangyu_dict)






