# by luffycity.com
# print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2)
#
# while 1:
#     pass
# else:
#     pass

# n = 66
# count = 1
# while count <= 3:
#     user_input = int(input("请输入一个数:"))
#     if user_input > n:
#         print("你猜大了")
#     elif user_input < n:
#         print("猜小了")
#     else:
#         print("恭喜你猜对了")
#         break
#     count = count + 1
# else:
#     print("太笨了你...")

# count = 1
# while count <= 10:
#     if count == 7:
#         pass
#     else:
#         print(count)
#     count = count + 1

# count = 1
# while count <= 10:
#     if count == 7:
#         count = count + 1
#         continue
#     print(count)
#     count = count + 1

# count = 1
# sum = 0
# while count <= 100:
#     sum = sum + count # 累加运算
#     count = count +1
# print(sum)

# count  = 1
# while count <= 100:
#     if count % 2 == 0:
#         print(count)
#     count = count + 1

# count = 1
# sum = 0
# while count <= 99:
#     if count % 2 == 1:  # 奇数
#         sum = sum + count
#     else: # 偶数
#         sum = sum - count
#     count = count + 1
# print(sum)

# count = 1 # 尝试的次数
# while count<= 3:
#     username = input("请输入用户名:")
#     password = input("请输入密码:")
#     if username == 'alex' and password == '123':
#         print("恭喜你. 登录成功")
#         break
#     else:
#         print("对不起, 用户名或密码错误!")
#         print("还剩下%s次登录机会" % (3-count))
#     count = count + 1


# ad = input("请输入广告标语:")
# if "最" in ad or "第一" in ad or "国家级" in ad or "稀缺" in ad:
#     print("广告不合法. 把设计人拉出去毙了")
# else:
#     print("OK的")


# 质数
n = int(input("请输入一个数:"))
if n == 1:
    print("不知道是不是")
else:
    count = 2
    while count <= n-1: # 质数只能被1和自身整除. 让这个数从2开始除. 一直除到n-1 如果除开了 一定不是质数 到最后还没有除开. 一定是质数
        if n % count == 0:
            print("你这个不是质数")
            break
        count = count + 1
    else:
        print("是一个质数")





