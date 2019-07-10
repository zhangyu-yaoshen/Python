import hashlib

# # 1. 创建一个MD5对象
# obj = hashlib.md5(b"flkjsdalkfjklasdjfklasjkflasdjklfasdjflkadsj") # 加盐
#
# # 2. 把要加密的内容给md5
# obj.update("alex".encode("utf-8")) # 必须是字节
#
# # 3. 获取密文
# val = obj.hexdigest()   # 534b44a19bf18d20b71ecc4eb77c572f aa7aa5ec13222b27f76a094207c5ac75
# print(val)

# def my_md5(val):
#     obj = hashlib.md5(b"flkjsdalkfjklasdjfklasjkflasdjklfasdjflkadsj")
#     obj.update(val.encode("utf-8"))
#     val = obj.hexdigest()
#     return val

# 注册的时候. 用md5进行加密. 存储的是加密后的密文
# username = input("请输入用户名")
# password = input("请输入密码")
# # cun = my_md5(password)
# # print(cun) # alex 26adff81aa6778d26999b95ddc0e50b2
# if username == "alex" and my_md5(password) == "26adff81aa6778d26999b95ddc0e50b2":
#     print("登录成功")
# else:
#     print("登录失败")

