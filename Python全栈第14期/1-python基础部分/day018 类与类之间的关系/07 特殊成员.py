# class Foo:
#     def __init__(self):
#         print("我是初始化")
#
#     def __call__(self, *args, **kwargs):
#         print("我是靠")
#
#     def __getitem__(self, item):
#         print("我是getitem", item)
#         return "大胖小子"
#     def __setitem__(self, key, value):
#         print(key, value)
#
#     def __delitem__(self, key):
#         print(key)
#
#     def __enter__(self):
#         print("我是进入")
#         return "周润发"
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("我是出来")


# 类名()  __init__() 构造方法
# obj = Foo()
# 对象() __call__()
# obj() # python特有的.
# 对象[xxx] 从对象中获取数据  默认执行__getitem__()

# 对象[xxx] = ,.... 默认执行__setitem__()
# obj["汪峰"] = "章子怡"

# del obj[key] 默认执行__delitem__()
# del obj['马化腾']



# dic = {"name":'汪峰', 'age':18}
# print(dic['name'])
#
# with obj as xx:
#     print(xx)
#     print("你好. 我叫周润发")

class Boy(object):
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return "name:%s, address:%s phone:%s" % (self.name, self.address, self.phone)

    def __new__(cls, *args, **kwargs):
        print("新概念")
        return object.__new__(cls) # 这句话才是创建对象.


b = Boy("alex",  "北京沙河", "10086")
print(b)



#
# lst = [123,456]
# print(lst)


