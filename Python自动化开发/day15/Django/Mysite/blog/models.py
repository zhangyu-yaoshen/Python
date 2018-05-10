from django.db import models

# Create your models here.

#ORM：对象关系映射【python的类-----数据表
#                   python的类实例-----表的记录
#                   python的类属性-----表的字段


#创建Books表
class Books(models.Model):
    #主键
    #nid=models.IntegerField(primary_key=True)
    #标题-字符串-32字节
    title=models.CharField(max_length=32)
    #作者
    author=models.CharField(max_length=32)
    #价格
    price=models.FloatField()
    #出版时间
    pub_date=models.DateField()






