#!/usr/bin/env python
# -*- coding:utf-8 -*-
v1 = [11,22,33,44,55,66,77,88,99,90]
v2 = {
    "k1":[],
    "k2":[],
}
for i in v1:
    if i > 66:
        v2["k1"].append(i)
    elif i < 66:
        v2["k2"].append(i)
print(v2)
