#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os#引用os模块
read_f = open("1.txt",encoding="utf-8",mode="r")#已读的方式打开原文件
write_f = open("2.txt",encoding="utf-8",mode="w")#以写的方式打开新文件
for line in read_f.readlines():
    if line.startswith("111"):#如果开头是道可道开头的
        line = "123456\n"#改成123456
    write_f.write(line)#把改好的值写道新的文件里2.
read_f.close()#关闭文件
write_f.close()#关闭文件
os.rename("1.txt","1b.txt")#把源文件备份
os.rename("2.txt","1.txt")#把2文件重命名为1文件

















