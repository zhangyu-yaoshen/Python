# # 递归
# def func():
#     print("我叫李嘉诚")
#     func() # 递归的入口
#
# # 调用函数
# func()

# 用递归实现1-100
# import sys
# sys.setrecursionlimit(5000) # 设置递归的最大深度, 一般不要改.
#
# def func(index):
#     print(index)
#     func(index + 1)
#
# func(1) # 递归的深度: 1000 但是到不了1000, 997 - 998



# 遍历某文件夹内的所有文件和文件夹

import os
# 树形结构的遍历
def func(file_path, ceng):
    # 获取到路径下的所有文件
    lst = os.listdir(file_path) # 得到文件夹里的所有文件和文件夹
    for file in lst: # 文件名
        # 获取到文件的全路径
        full_path = os.path.join(file_path, file) # D:\python学院\s16\第一阶段\day01 认识python 变量 数据类型 条件if语句
        if os.path.isdir(full_path): # 判断这个路径是否是一个文件夹
            print("\t"*ceng, file)
            func(full_path, ceng+1)
        else:
            print("\t"*ceng, file)
    else:
        return
func("D:\python学院\s16\第一阶段", 0)

