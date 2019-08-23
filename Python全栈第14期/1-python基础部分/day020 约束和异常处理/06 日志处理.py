#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging

logging.basicConfig(filename='app.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=40)    # level 设置级别. 当你的信息的级别>=level的时候才会写入日志文件, 默认30

# # # CRITICAL = 50
# # # FATAL = CRITICAL
# # # ERROR = 40
# # # WARNING = 30
# # # WARN = WARNING
# # # INFO = 20
# # # DEBUG = 10
# # # NOTSET = 0
# # # 写日志
# logging.critical("我是critical")
# logging.error("我是error")
# logging.warning("我是警告")
# logging.info("我是基本信息")
# logging.debug("我是调试")
# logging.log(2, "我是自定义")


# import traceback
# #
# for i in range(20):
#     try:
#         if i % 3 == 0:
#             raise FileNotFoundError("我是FileNotFountException")
#         elif i % 3 == 1:
#             raise StopIteration()
#         elif i % 3 == 2:
#             raise KeyError()
#
#     except FileNotFoundError as e:
#         val = traceback.format_exc()
#         logging.error(val)
#     except StopIteration as e:
#         val = traceback.format_exc()
#         logging.error(val)
#     except KeyError as e:
#         val = traceback.format_exc()
#         logging.error(val)
#     except Exception as e:
#         val = traceback.format_exc()
#         logging.error(val)


# 多文件日志处理
# 创建⼀个操作⽇志的对象logger（依赖FileHandler）
file_handler = logging.FileHandler('l1.log', 'a', encoding='utf-8')
# 设置日志文件内容的格式
file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s: %(message)s"))
logger1 = logging.Logger('A', level=40)
logger1.addHandler(file_handler)
# 记录日志
logger1.error('我是A系统')



# 再创建⼀个操作⽇志的对象logger（依赖FileHandler）
file_handler2 = logging.FileHandler('l2.log', 'a', encoding='utf-8')
file_handler2.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s -%(levelname)s -%(module)s: %(message)s"))
logger2 = logging.Logger('B', level=40)
logger2.addHandler(file_handler2)
# 记录日志
logger2.error('我是B系统')




