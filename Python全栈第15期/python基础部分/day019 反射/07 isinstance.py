class Animal:
    pass

class Cat(Animal):
    pass

class BoSiCat(Cat):
    pass

# a = Animal()
# print(isinstance(a, Animal)) # 自己类可以判断
# print(isinstance(a, Cat))   # 子类不能判断



c = BoSiCat()
print(isinstance(c, Animal)) # True  子类的对象可以当成父类的类型来看.
# isinstance判断的是对象是否是xxx家族体系的内容. 往上找




lst = "马化腾"
print(type(lst.__iter__()))








