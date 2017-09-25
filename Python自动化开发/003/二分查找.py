#!/usr/bin/env python
# -*- coding:utf-8 -*-
#二分半查询
data = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]
def binary_search(find_str,data_set,count):
    mid = int(len(data_set)/2)#列表的长度除以2；找到列表中间的索引值；并属于int类型
    if mid == 0:
        if data_set[mid] == find_str:
            print("find it finally",find_str,count)
        else:
            print("cannot find this num in list",find_str,count)
        return
    if data_set[mid] == find_str:#如果要找的值就是这个索引值
        print("find it",find_str,mid)
    elif data_set[mid] > find_str:
        print("going to search in left",data_set[mid],data_set[0:mid])
        binary_search(find_str,data_set[0:mid],count+1)
    else:
        print("going to search in right",data_set[mid],data_set[mid+1:])
        binary_search(find_str, data_set[mid+1:], count + 1)

binary_search(11,data,0)#调用函数【要差的数字，从哪个列表查，查找的次数】





