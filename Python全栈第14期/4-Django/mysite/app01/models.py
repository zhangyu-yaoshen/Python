from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)   # -> 创建一个自增的ID列作为主键
    email = models.CharField(max_length=24)  # -> varchar(32)
    pwd = models.CharField(max_length=16)  # -> varchar(32)
    def __str__(self):
        return self.email

# 出版社
class Press(models.Model):
    id = models.AutoField(primary_key=True)  # id主键
    name = models.CharField(max_length=32)  # 出版社名称

    def __str__(self):
        return '<这是一个出版社对象，它的名字是:{}>'.format(self.name)

# 书
class Book(models.Model):
    id = models.AutoField(primary_key=True)  # 自增id主键
    title = models.CharField(max_length=30)  # 书名
    # Django 1.11 默认就是级联删除， Django 2.0之后必须指定on_delete
    # to=关联的表名【关联出版社表】
    press = models.ForeignKey(to='Press', on_delete=models.CASCADE)

