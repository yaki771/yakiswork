# Generated by Django 3.1.2 on 2021-01-09 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210108_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='交通工具',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=70)),
            ],
        ),
        migrations.AlterField(
            model_name='homework',
            name='交通工具',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.交通工具'),
        ),
    ]
