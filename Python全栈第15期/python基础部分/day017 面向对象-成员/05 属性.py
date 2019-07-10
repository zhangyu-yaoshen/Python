class Person:

    def __init__(self, name, num, gender, birthday):
        self.name = name
        self.num = num
        self.gender = gender
        self.birthday = birthday


    @property # 表示当前方法是一个属性. 方法的返回值就是这个属性的值
    def age(self): # 方法只能有一个参数, self
        return 10 # 必须有返回值


p = Person("alex", "10086", "不详", "1989年12月1日")
print(p.age) # 可以直接访问属性, 实际上访问的是age()方法. 返回值就是属性值