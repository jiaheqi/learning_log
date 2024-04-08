from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Topic(models.Model):  # 继承Model，即Django中定义了模型基本功能的类
    """用户学习主题"""
    text = models.CharField(max_length=200)  # 由字符组成的数据，即文本
    date_added = models.DateTimeField(auto_now=True)  # 日期和时间的数据,参数属性表示自动设置当前日期和时间
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # 建立到模型User的外键关系。用户被删除时，所有与之相关联的主题也会被删除

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text  # 告诉Django，默认使用哪个属性来显示有关主题的信息


class Entry(models.Model):
    """学到的某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # 外键(foreign key)是一个数据库术语，它指向数据库中的另一条记录，这里是将每个条目关联到特定主题
    # 创建每个主题时，都分配了一个键(ID)。需要在两项数据之间建立联系时，Django使用与每项信息相关联的键.
    # on_delete=models.CASCADE让Django在删除主题的同时删除所有与之相关联的条目，这称为级联删除(cascading delete)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'entries'
        # Django在需要时使用Entries来表示多个条目。如果没有这个类，Django将使用Entrys来表示多个条目

    def __str__(self):
        """返回字符串表示"""
        return f"{self.text[:50]}..."
