from django.db import models
import django.utils.timezone as timezone
from django.contrib.auth.models import User, Group

# Create your models here.


class Topic(models.Model):
    '''单位工程名称'''
    text = models.CharField(max_length=200,
                            verbose_name='工程名称')
    date_added = models.DateField(default=timezone.now)
    company = models.ForeignKey(Group, on_delete=models.CASCADE,
                                verbose_name='施工单位')
    owner = models.ManyToManyField(User, verbose_name="管理员")
    '''增加单位工程属性'''
    quantity = models.FloatField(default=0, verbose_name='工 程 量')
    character = models.CharField(max_length=255, verbose_name='技术特征')
    start_time = models.DateField(default=timezone.now, verbose_name='开工时间')
    end_time = models.DateField(default=timezone.now, verbose_name='完工时间')
    days = models.IntegerField(default=0, verbose_name='工期(天)')

    class Meta:
        verbose_name = '单位工程'
        verbose_name_plural = '单位工程'

    def __str__(self):
        return self.text


class Entry(models.Model):
    '''施工日报'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='工程名称')
    company = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='施工单位')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='记录人')
    text = models.TextField(verbose_name='施工日报')
    date_added = models.DateField(default=timezone.now, verbose_name='施工日期')
    '''增加日报细分内容'''
    worker = models.IntegerField(verbose_name='出勤人数')
    footage = models.FloatField(default=0, verbose_name='工程进度')
    rock = models.FloatField(default=0, verbose_name='出矸量')
    water = models.FloatField(default=0, verbose_name='排水量')
    cement = models.FloatField(default=0, verbose_name='水泥/砼量')

    class Meta:
        verbose_name = '施工日报'
        verbose_name_plural = '施工日报'

    def __str__(self):
        """返回日报前20字"""
        self.text[:20]
        '''
        if len(self.text) > 20:
            return  + "..."
        else:
            return self.text[:20]
        '''
