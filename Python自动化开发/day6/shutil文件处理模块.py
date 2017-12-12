#!/usr/bin/env python
# -*- coding:utf-8 -*-
import shutil
#高级的 文件、文件夹、压缩包 处理模块

"""
shutil.copyfileobj(fsrc, fdst[, length])
将文件内容拷贝到另一个文件中，可以部分内容
fsrc【原文件对象】
fdst【目标文件对象】
length【长度】
"""
# f1 = open("daodejing",encoding="utf-8")
# f2 = open("ddj.txt","w",encoding="utf-8")
# shutil.copyfileobj(f1,f2)

"""
拷贝文件
原文件名，目标文件名
"""
# shutil.copyfile("daodejing","ddj-01.txt")

"""
shutil.ignore_patterns(*patterns)
shutil.copytree(src, dst, symlinks=False, ignore=None)
递归的去拷贝文件
src:源文件
dst:目标文件
symlinks:
ignore:过滤掉不复制的文件
#复制QQQ文件到ABC；logger.py不复制
"""
# shutil.copytree("E:\\Python\Python自动化开发\day5\QQQ",
#                 "E:\\Python\Python自动化开发\day6\ABC",
#                 ignore=shutil.ignore_patterns("logger.py"))

"""
base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
如：www                        =>保存至当前路径
如：/Users/wupeiqi/www =>保存至/Users/wupeiqi/
format：    压缩包种类，“zip”, “tar”, “bztar”，“gztar”
root_dir：    要压缩的文件夹路径（默认当前目录）
owner：    用户，默认当前用户
group：    组，默认当前组
logger：    用于记录日志，通常是logging.Logger对象
"""
#shutil.make_archive("day5","zip","E:\\Python\Python\Python\Python自动化开发\day5")
































