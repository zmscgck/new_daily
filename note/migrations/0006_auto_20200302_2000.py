# Generated by Django 3.0.3 on 2020-03-02 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_auto_20200302_1958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='guantity',
            new_name='quantity',
        ),
    ]
