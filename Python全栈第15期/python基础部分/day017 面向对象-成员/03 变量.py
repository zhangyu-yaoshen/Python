class Person:
    country = "中国"  # 类变量. 不属于对象, 对象可以访问.

    def __init__(self, name, num, gender, birthday):
        # 成员变量(实例变量)
        self.name = name
        self.num = num
        self.gender = gender
        self.birthday = birthday

    # 对象来访问（成员方法）（实例方法）
    def marray(self, duifang):
        print("人会结婚%s" % duifang)

alex = Person("李杰", 10086, "男", "昨天")
alex.country = "澳大利亚" # 注意。 这里和类变量没由一毛钱关系, 给alex单独加一个属性叫country = ”澳大利亚“

wusir = Person("吴佩琪", 10010, "女", "今天")

print(alex.country) # 澳大利亚 # 拿到的是自己的。成员实例变量 字段
print(wusir.country) # 中国
print(Person.country)   # 中国

# 总结：类变量，用类名去操作. 规范.
