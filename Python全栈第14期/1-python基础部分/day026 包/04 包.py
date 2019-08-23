# from urllib.request import urlopen # 点 前面的一定是包
# 包其实就是文件夹

# from urllib import request
# request.urlopen()

# 导入包要根据你的实际情况
# 包就是一个文件夹, 文件夹内部要有一个__init__.py
# 在py2中这个__init__.py是强制的.  py3里面可以没有这个文件
# 自己定义一个包的话. 一定要给出__init__.py

# 创建包:
#   创建文件夹
#   创建__init__.py
# 使用pycharm可以直接创建python的package(包)

# import haha # 导入一个包的时候默认执行的是__init__.py文件



# import os
# os.makedirs('glance/api')
# os.makedirs('glance/cmd')
# os.makedirs('glance/db')
# l = []
# l.append(open('glance/__init__.py','w'))
# l.append(open('glance/api/__init__.py','w'))
# l.append(open('glance/api/policy.py','w'))
# l.append(open('glance/api/versions.py','w'))
# l.append(open('glance/cmd/__init__.py','w'))
# l.append(open('glance/cmd/manage.py','w'))
# l.append(open('glance/db/__init__.py','w'))
# l.append(open('glance/db/models.py','w'))
# map(lambda f:f.close() ,l)

# import glance.api.policy
# # glance.api.policy.get()

# from glance.api.policy import get
#
# def get():
#     print("我是get")
#
# get()

# import glance # 导入包的时候. 默认执行的是__init__.py
# print(glance.money)
# glance.hello()

# from glance import *
# print(money)
# hello()

# import glance
# glance.api.policy.get()


# sys.path 是随动. 根据启动脚本所在的文件夹.

# 找glance里面的cmd 导入manage
# sys.path -> day026 包
# import glance.api.policy

# import glance.api.versions

# 当你有一天写出来一个完整的框架级的功能. 很牛B的时候. 封装出来的包一般内部使用相对路径.
# 后面学习的高级框架.内部使用的大多数是相对路径.

# 你用别人写好的框架. 你要用绝对导入.

import glance
glance.api.policy.get()


