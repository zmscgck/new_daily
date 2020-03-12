# Generated by Django 3.0.3 on 2020-03-02 11:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_auto_20200208_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='cement',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='entry',
            name='footage',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='entry',
            name='rock',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='entry',
            name='water',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='entry',
            name='worker',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='topic',
            name='character',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
        ),
        migrations.AddField(
            model_name='topic',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='topic',
            name='guantity',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='topic',
            name='plan',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='topic',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
