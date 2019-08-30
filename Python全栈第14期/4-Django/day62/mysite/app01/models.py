from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)   # -> 创建一个自增的ID列作为主键
    email = models.CharField(max_length=24)  # -> varchar(32)
    pwd = models.CharField(max_length=16)  # -> varchar(32)

    def __str__(self):
        return self.email


# 出版社表
class Press(models.Model):
    id = models.AutoField(primary_key=True)  # id主键
    name = models.CharField(max_length=32)  # 出版社名称

    def __str__(self):
        return '<这是一个出版社对象，它的名字是:{}>'.format(self.name)


# 书
class Book(models.Model):
    id = models.AutoField(primary_key=True)  # 自增id主键
    title = models.CharField(max_length=30)  # 书名
    price = models.IntegerField()  # 价格
    # Django 1.11 默认就是级联删除， Django 2.0之后必须指定on_delete
    # to=关联的表名
    press = models.ForeignKey(to='Press', on_delete=models.CASCADE)


# 作者
class Author(models.Model):
    id = models.AutoField(primary_key=True)  # 自增id主键
    name = models.CharField(max_length=32)  # 作者名字
    books = models.ManyToManyField(to='Book')  # 只是ORM层面建立的一个多对多关系，不是作者表的一个字段

    def __str__(self):
        return self.name


# 创建作者和书籍的关系表
# class Author2Book(models.Model):
#     id = models.AutoField(primary_key=True)
#     author = models.ForeignKey(to='Author', on_delete=models.CASCADE)
#     book = models.ForeignKey(to='Book', on_delete=models.CASCADE)