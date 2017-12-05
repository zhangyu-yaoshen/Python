#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import random
# print(random.randint(1,10))#打印1到10的随机数
# print(random.randrange(1,20,2))#打印1到20之间的随机数；步长是2
# print(random.sample(range(100),5))#随机5个数；100以内的


# #生成随机验证码
# import random
# checkcode = ''
# for i in range(4):#生成四位的验证码
#     current = random.randrange(0,4)#随机0到4之间的值
#     if current != i:#如果这个值不等于i
#         temp = chr(random.randint(65,90))#65到90时A到Z的对应值
#     else:#如果这个值等于i
#         temp = random.randint(0,9)#随机0到9的随机值
#     checkcode += str(temp)
# print(checkcode)

import random,string
print(string.ascii_uppercase)#ascii码里的大写A到Z
print(string.ascii_letters)#ascii码里的大写和小写A到Z
print(string.ascii_lowercase)#ascii码里的小写A到Z
print(string.digits)#所有的数字
print(string.digits+string.ascii_lowercase)#所有的数字和ascii码里的小写A到Z

#生成随机验证码
source = string.digits+string.ascii_lowercase
print("".join(random.sample(source,6)))
