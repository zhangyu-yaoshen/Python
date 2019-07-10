# # (1)过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
# lst = ["alex", "eggon", "sb", "wusir", "dsb", "xsb"]
#
# new_lst = [ el.upper() for el in lst if len(el) > 3]
# print(new_lst)
#
# # (2)求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表
# lst = [(x, y) for x in range(5) for y in range(6) if x%2==0 and y % 2 == 1]
# print(lst)

#          2 1 0   2 1 0   2 1 0
# (3)M = [[1,2,3],[4,5,6],[7,8,9]]
# M = [[1,2,3],[4,5,6],[7,8,9]]
#
# result = [lst[2] for lst in M]
# print(result)

# M = [3, 6, 9]
# print([[i-2,i-1,i] for i in M])


# lst = [ i * i for i in range(50) if i % 3 == 0]
#
# lst = ["python%s期" % i for i in range(1, 11) if i != 5]

# l1 = ['alex', 'WuSir', '老男孩', '太白']
# lst = [l1[i] + str(i) for i in range(len(l1))]
# print(lst)


x = {
    'name':'alex',
    'Values':[{'timestamp':1517991992.94,
         'values':100,},
        {'timestamp': 1517992000.94,
        'values': 200,},
        {'timestamp': 1517992014.94,
         'values': 300,},
        {'timestamp': 1517992744.94,
         'values': 350},
        {'timestamp': 1517992800.94,
         'values': 280}
		]
}

lst = [[el['timestamp'], el['values']] for el in x['Values']]
print(lst)



