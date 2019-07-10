# import 文件名(模块名)
# import 之后做了些什么事儿?
# 1. 先检查是否已经加载过了这个模块, sys.modules
# 2. 如果没有导入过. 创建这个模块的名称空间
# 3. 把这个模块中的代码执行一遍. 生成的所有东西都放在刚才的内存空间中
# 4. 当没有as的时候是使用模块的名字来引用这个名称空间. 当有as的时候. 用as的名字命名空间
# import yitian as yt
#
# print(yt.main_person_man)


# import yitian
# print(globals()) # 也可以查看当前空间中引入的内容


# # 模块的加载顺序: 从内存里找. -> 内置 -> sys.path
# import sys
# print(sys.modules.keys()) # 查看到已经引入的模块信息
# print(sys.path)

# import yitian
#
# # print(__name__) # __main__  模块名
# main_person_man = "1231"
# if __name__ == '__main__': # __main__ 程序的入口
#     print("我在浪挖的测试")

# if name == "mysql":
#     import mysql as db
# elif name == "oralce":
#     import oracle as db
#
# db.connet()
# db.xxx
# db.close()

# import time, json, re, yitian
#
# print(time.time())

from yitian import main_person_man
# from yitian import fight_on_light_top
# from yitian import * # import后面可以跟上* 所有
# import yitian
main_person_man = "灭绝" #  引入的名字和自己的变量是冲突的
print(main_person_man)
# fight_on_light_top()

import time
# print(time.time())

from time import *
print(time())


# 包





