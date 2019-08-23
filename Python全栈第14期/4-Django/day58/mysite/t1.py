#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Name    : t1.py
Author  : Python
Time    : 2019/8/20 0020 17:46
"""
import os
# os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
test_os = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

test_os1 = os.path.dirname(os.path.abspath(__file__))
test_os2 = os.path.dirname
test_os3 = os.path.abspath(__file__)
print(test_os)
print(test_os1)
print(test_os2)
print(test_os3)