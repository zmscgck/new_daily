# Generated by Django 3.0.4 on 2020-03-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img_db', '0002_auto_20200320_1426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='img',
            options={'verbose_name': '工程图片', 'verbose_name_plural': '工程图片'},
        ),
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.ImageField(upload_to='img', verbose_name='图片'),
        ),
    ]
