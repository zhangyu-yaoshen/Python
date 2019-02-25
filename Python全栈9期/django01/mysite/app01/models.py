from django.db import models

# Create your models here.
# ORM相关的只能写在这个文件里，写到别的文件里Django找不到
# 类必须继承models.Model
class UserInfo(models.Model):#UserInfo表名
    id = models.AutoField(primary_key=True)     #创建一个自增的主键字段
    name = models.CharField(null=False, max_length=32)        #创建一个varchar类型的不能为空,最大长度为20的字段

