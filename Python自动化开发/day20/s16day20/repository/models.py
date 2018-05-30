from django.db import models

#用户表
class UserInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    #用户名32字节；unique=True是唯一索引；不能重复
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32, unique=True)
    ctime = models.DateTimeField()

    class Meta:
        verbose_name_plural = '用户表'

    def __str__(self):
        return self.username
#新闻类型表
class NewsType(models.Model):
    nid = models.AutoField(primary_key=True)

    caption = models.CharField(max_length=32)
    class Meta:
        verbose_name_plural = "新闻类型"

    def __str__(self):
        #admin显示填写的类型caption
        return self.caption
#新闻表
class News(models.Model):
    nid = models.AutoField(primary_key=True)
    #这两个表示谁创建的；和什么类型的；关联哪个表
    user_info = models.ForeignKey('UserInfo')
    news_type = models.ForeignKey('NewsType')
    #新闻标题
    title = models.CharField(max_length=32, db_index=True)
    #新闻跳转到哪个url；可以为空
    url = models.CharField(max_length=128, null=True,blank=True)
    #简介
    content = models.CharField(max_length=50)
    #点赞个数；喜欢
    favor_count = models.IntegerField(default=0)
    #评论个数
    comment_count = models.IntegerField(default=0)
    #时间戳
    ctime = models.DateTimeField()
    class Meta:
        verbose_name_plural = '新闻'

    def __str__(self):
        return self.title
#点赞
class Favor(models.Model):
    nid = models.AutoField(primary_key=True)
    #关联表
    user_info = models.ForeignKey('UserInfo')
    news = models.ForeignKey('News',related_name='favor_users')

    ctime = models.DateTimeField(null=True,blank=True)

    #
    class Meta:
        verbose_name_plural = '点赞记录'
        #联合唯一索引；一个人只能对一个新闻点赞一条
        unique_together = (
            ("user_info", "news"),
        )
#评论
class Comment(models.Model):
    nid = models.AutoField(primary_key=True)
    #关联表
    user_info = models.ForeignKey('UserInfo')
    news = models.ForeignKey('News')

    ctime = models.DateTimeField()
    #设备
    device = models.CharField(max_length=16,null=True,blank=True)
    content = models.CharField(max_length=150)
    #评论id【子级评论】
    reply_id = models.ForeignKey('Comment', related_name='b', null=True, blank=True)

    class Meta:
        verbose_name_plural = '评论表'


"""
comment_list = Comment.objects.filter(news_id=1)
ID      新闻ID    用户ID       评论给内容
1         1        10           写的什么玩意呀
2         1        11           还真不是玩意
3         1        12           写的真好
4         1        11           我总算看明白了，原来是我智商低
"""



"""
ID      新闻ID    用户ID       评论给内容                             reply_id
1         1        10           写的什么玩意呀                          null
2         1        11           还真不是玩意                             1
3         1        12           写的真好                                 1
4         1        11           我总算看明白了，原来是我智商低            3
"""



# 写的什么玩意呀
#     - 还真不是玩意
#     - 写的真好
#         - 我总算看明白了，原来是我智商低
#     - sdf













