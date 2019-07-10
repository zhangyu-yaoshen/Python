# import os

# 创建多级目录
# os.makedirs("a/b/c/d/e/f/g")
# os.removedirs("a/b/c/d/e/f/g") # 空目录可以删除. 非空的不能删

# os.system("dir") # 执行命令
# ret = os.popen("dir").read() # 执行命令返回结果
# print(ret)

# print(os.getcwd())

# print(os.path.split(r"D:\python学院\s16\第一阶段\day08 文件操作\video"))
# print(os.path.exists(r"D:\python学院\s16\第一阶段\day08 文件操作\video12312312312321"))

# print(os.name)  # nt NT windows平台
#
# import sys
# # print(sys.version)
# print(sys.path) # 获取系统搜索模块的路径
# sys.path.clear() # 应该是没了的.
# import os
# print(os.name)
#
# # sys.platform = "刘伟"
# print(sys.platform)
import sys

print(sys.argv)  # 在运行的时候给python传递的信息.
ip = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]

print(ip)
print(username)
print(password)

