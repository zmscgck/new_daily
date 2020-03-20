from django.db import models
import django.utils.timezone as timezone
from django.contrib.auth.models import User, Group
# Create your models here.


class IMG(models.Model):
    img = models.ImageField(upload_to='img', verbose_name='图片')
    name = models.CharField(max_length=200, verbose_name='图片说明')
    company = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='施工单位')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='上传人')
    date_added = models .DateField(default=timezone.now)


    class Meta:
        verbose_name = '工程图片'
        verbose_name_plural = '工程图片'