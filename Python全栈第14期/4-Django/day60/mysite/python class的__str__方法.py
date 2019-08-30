class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '{}:{}'.format(self.name, self.age)


p1 = Person('黄袍哥', 18)
print(p1)
