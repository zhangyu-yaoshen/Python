import shelve

# 打开一个文件
# f = shelve.open("大阳哥", writeback=True)
# f['jj'] = "林俊杰"
# f['dyg'] = "大阳哥"
# f['zzr'] = "周芷若"

# f = {}
# 像操作字典一样操作文件
# f["jay"] = "周杰伦"
# print(f['jay'])

# f["jay"] = {'name': "周杰伦", 'age': 38, "hobby": "吃喝拉撒睡"}

# f['jay']['name'] = "胡辣汤"
# print(f['jay']['name'])
# print(f['jay'])


# f.close()

f = shelve.open("大阳哥")
# print(f.keys())
# for k in f.keys(): # 可以获取到所有的key
#     print(k)
#
# for k in f:
#     print(k)
#
# for k, v in f.items():
#     print(k, v)
