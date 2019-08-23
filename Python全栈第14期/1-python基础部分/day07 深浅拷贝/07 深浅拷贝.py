# lst1 = ["太白","日天","哪吒","银王","金王"]
# lst2 = lst1
# lst1.append("女神")
# print(id(lst1))
# print(id(lst2))

# lst1 = ["太白","日天","哪吒","银王","金王"]
# # lst2 = lst1[:]  # 创建了新列表
# lst2 = lst1.copy() # 会创建新对象, 创建对象的速度会很快.
# lst1.append("女神")
# print(lst1)
# print(lst2)

# 浅拷贝
# lst1 = ["太白","日天",["盖浇饭", "锅包肉", "吱吱冒油的猪蹄子"],"哪吒","银王","金王"]
# lst2 = lst1.copy() # 会创建新对象, 创建对象的速度会很快.
# lst1[2].append("油泼扯面")
# print(lst1)
# print(lst2)
# print(id(lst1[2]), id(lst2[2]))

# 深拷贝
#导入拷贝模块
import copy
lst1 = ["太白","日天",["盖浇饭", "锅包肉", "吱吱冒油的猪蹄子"],"哪吒","银王","金王"]
lst2 = copy.deepcopy(lst1)
lst1[2].append("油泼扯面")
print(lst1)
print(lst2)
print(id(lst1[2]), id(lst2[2]))

# 赋值没有创建新对象。多个变量共享同一个对象
# 浅拷贝。 会创建新对象。 新的对象中里面的内容不会被拷贝
# 深拷贝。 创建一个一摸一样的完全新的对象。 这个对象延伸出来的内容也会跟着复制一份


# a = [1, 2]
# a[1] = a
# print(a[1])
