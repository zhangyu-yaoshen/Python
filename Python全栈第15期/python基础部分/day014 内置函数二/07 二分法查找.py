# 二分法查找的效率特别高.
# 缺点: 有序序列
#
# lst = [1,8,16,32,55,78,89,1,5,4,7,5,9,6,8,5,4,5,44,5,2,1,4,5,1]
# # [1, 1, 1, 1, 2, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 7, 8, 8, 9, 16, 32, 44, 55, 78, 89]
# lst = sorted(lst)
# n = int(input("请输入一个数:"))
# left = 0
# right = len(lst) - 1
#
# while left <= right: #
#
#     mid = (left + right) // 2  # 索引只能是整数
#     if n > lst[mid]:
#         left = mid + 1
#     elif n < lst[mid]:
#         right = mid - 1
#     else:
#         print("在这个列表中.所在的位置%s" % mid)
#         break
# else:
#     print("你要找的数. 不在这个序列中")


# 递归的第一套方案
# def func(n, lst):
#     left = 0
#     right = len(lst) - 1
#     if left <= right:
#         mid = (left + right)//2
#         if n > lst[mid]:
#             new_lst = lst[mid+1:]
#             return func(n, new_lst)
#         elif n < lst[mid]:
#             new_lst = lst[:mid]
#             return func(n, new_lst)
#         else:
#             print("刚刚好, 在这里出现了")
#             return True
#     else:
#         return False
#
# lst = [1, 1, 1, 1, 2, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 7, 8, 8, 9, 16, 32, 44, 55, 78, 89]
# ret = func(2, lst)
# print(ret)

# 第二套方案
def func(n, lst, left=0, right=None):
    if right == None:
        right = len(lst) - 1
    if left <= right:
        mid = (left + right) // 2
        if n > lst[mid]:
            left = mid + 1
        elif n < lst[mid]:
            right = mid - 1
        else:
            return True
        return func(n, lst, left, right)
    else:
        return False


lst = [1, 1, 1, 1, 2, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 7, 8, 8, 9, 16, 32, 44, 55, 78, 89]
ret = func(98, lst)
print(ret)
