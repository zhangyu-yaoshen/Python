#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import hashlib
# #MD5算法值
# m = hashlib.md5()
# m.update(b"hello")#16进制【5d41402abc4b2a76b9719d911017c592】
# print (m.hexdigest())

import hmac
h = hmac.new('天王盖地虎'.encode("utf-8"), '宝塔镇河妖'.encode("utf-8"))
print(h.hexdigest())#5f90dcd2211cd11601ce05195e3c5232



