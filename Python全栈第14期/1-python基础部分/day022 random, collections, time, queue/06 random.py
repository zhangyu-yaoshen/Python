import random

# print(random.random()) #  0-1小数  想办法完成[1,100]之间的随机整数
# print(random.uniform(1, 3)) # 1-3之间的小数
#
# print(random.randint(1, 36)) # [1,36]随机整数
# print(random.randrange(1, 5, 3)) # [1, 5) 步长是3


print(random.choice(["马化腾", ["倚天屠龙记", "天龙八部", "射雕"], "张无忌", "周伯通", "刘伟"])) # 随机选一个
print(random.sample(["刘伟", "大阳哥", "大猪蹄子", "胡辣汤"], 3))
print(random.sample(list(range(1,37)), 7))


# lst = [1,2,3,4,5,5,6,7,8,9,]
# random.shuffle(lst) # 洗牌
# print(lst)
