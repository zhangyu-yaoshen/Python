#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield#接收到producer的send过来的值；赋值给baozi变量
       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

def producer(name):
    c = consumer('A')#定义消费者
    c2 = consumer('B')#定义消费者
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)#调用next；并给yield传值
        c2.send(i)

producer("zhangyu")











