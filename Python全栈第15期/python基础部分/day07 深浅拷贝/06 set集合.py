# dic = {"a":"哇哈哈", "a":"爽歪歪"}
# print(dic) # key 不会重复
# dic[[1,2,3]] = "哇哈哈" # 必须是可哈希的

# s = set() # 空集合
# s = {1,2,3,6,3,4,6,4, [4,5,6]} # 不重复, 必须是可哈希的
# print(s)

# set其实就是不存value的字典. 只存key
# 去重复
# lst = [1,2,3,4,4,4,4,5,5,6,7,7,7]
# s = set(lst)
# lst = list(s)
# print(lst)

s = {"赵本山", "范伟", "小沈阳", "高秀敏", "宋小宝"}
# s.add("赵铁柱")
# s.add("李小花")
# s.add("王尼玛")
# s.add("张全蛋")
# print(s)
#
# s.update(("刘伟", '张伟', "张三丰")) # 迭代更新

# item = s.pop()
s.remove("小沈阳")
print(s)
# print(item)

# for el in s:
#     print(el)
