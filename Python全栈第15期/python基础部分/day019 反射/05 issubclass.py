class Animal:
    pass

class Cat(Animal):
    pass

class BoSiCat(Cat):
    pass


print(issubclass(Cat, Animal)) # 判断第一个参数是否是第二个参数的后代
print(issubclass(Animal, Cat))
print(issubclass(BoSiCat, Animal)) # True
