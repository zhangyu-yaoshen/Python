#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
logger = logging.getLogger("simple_example")#设置日志名字
logger.setLevel(logging.DEBUG)#设置全局的日志级别

#设置显示器
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

#设置文件
fh = logging.FileHandler("log.log")
fh.setLevel(logging.INFO)

#设置日志格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)#设置显示器的日志格式
fh.setFormatter(formatter)#设置文件的日志格式

#将指定的处理程序添加到全局变量logger执行
logger.addHandler(ch)
logger.addHandler(fh)

#打印日志级别
logger.debug('debug msg...')
logger.info('info msg...')
logger.warning('warning msg...')
logger.error('error msg...')
logger.critical('critical msg...')
logger.log(10,'log msg...')













