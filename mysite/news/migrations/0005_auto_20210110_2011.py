# Generated by Django 3.1.2 on 2021-01-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210109_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='交通工具',
            field=models.CharField(default='方式', max_length=200),
        ),
        migrations.DeleteModel(
            name='交通工具',
        ),
    ]