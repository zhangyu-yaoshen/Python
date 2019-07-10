# import random
#
# lst = []
# for i in range(48,58):
#     lst.append(chr(i))
#
# for i in range(ord("a"), ord("z") + 1):
#     lst.append(chr(i))
#
# for i in range(ord('A'), ord('Z') + 1):
#     lst.append(chr(i))
#
# print(random.sample(lst, 4))

# import random
#
# money = 100
# ren = 30
# qian_moneny = 0
#
# lst = []
# for i in range(ren-1):
#     m = random.uniform(0, money - qian_moneny)
#     qian_moneny += m
#     lst.append(m)
#
# lst.append(money - qian_moneny)
# print(lst)

# import random
# def bonus(person,money):
#     dic = {}
#     num_sum = 0
#     for i in range(person):
#         num = random.randint(1,100) #在1-100随机整数
#         dic["Person%s"%(i+1)] = num
#         num_sum += num
#
#     for el in dic: #1/6
#         x =round(dic[el]/num_sum*money,2)
#         dic[el] = x
#     return dic
#
# result = bonus(10,10)
# print(result)


# def outer():
#     content = "1111"
#     def inner():
#         print(content)
#
#     return inner
#
# fn = outer()
# fn()
# fn()
# fn()
# fn()
#
# import json
# from urllib.request import urlopen
#
# content = urlopen("https://h5.ele.me/restapi/shopping/v2/restaurants/search?offset=15&limit=15&keyword=%E7%9B%96%E6%B5%87%E9%A5%AD&latitude=39.904172&longitude=116.407417&search_item_type=3&is_rewrite=1&extras[]=activities&extras[]=coupon&terminal=h5").read()
#
# s = content.decode("utf-8")
# dic = json.loads(s)
#
# rwf = dic['inside']['0']['restaurant_with_foods']
# for el in rwf:
#     # 那商家
#     print(el['restaurant']['name']) #  店铺名称
#     for food in el['foods']:
#         print(food['name'])

print(r"周润发\n李\t嘉\r诚") # r能取消掉转义

