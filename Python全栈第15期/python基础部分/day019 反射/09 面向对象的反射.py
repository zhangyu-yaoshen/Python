
class Person:
    def __init__(self, name):
        self.name = name
        self.age = None

    def chi(self):
        print("人喜欢吃东西%s" % self.name)

p = Person("刘伟")
setattr(p, "name", "大阳哥") # 动态的给对象设置属性和值
setattr(p, "age", 18) # 很少用. 慎用

print(p.age)
delattr(p, "age")
print(p.age)

# p.chi()

# val = input("请输入你想让刘伟执行的动作:")
# if hasattr(p, val):
#     getattr(p, "name")
#     func = getattr(p, val)
#     func()





