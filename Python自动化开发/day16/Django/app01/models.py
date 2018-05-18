from django.db import models

# Create your models here.


#创建Books表
class UserInfo(models.Model):
    #默认创建id列；自增；主键
    #用户名列；字符串类型；指到长度
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)



    # #主键
    # #nid=models.IntegerField(primary_key=True)
    # #标题-字符串-32字节
    # title=models.CharField(max_length=32)
    # #作者
    # author=models.CharField(max_length=32)
    # #价格
    # price=models.FloatField()
    # #出版时间
    # pub_date=models.DateField()





