'''
from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
    '''
from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=70,default='', verbose_name='姓名')
    #age = models.IntegerField()
    class Sex(models.IntegerChoices):
        MALE = 1, '男'
        FEMALE = 2, '女'
        OTHER = 3, '其他'

    sex = models.IntegerField(choices=Sex.choices)

    def __str__(self):
        return self.full_name

class 交通工具(models.Model):
    vehicle = models.CharField(max_length=70,default='', verbose_name='姓名')
    #age = models.IntegerField()
   
    def __str__(self):
        return self.vehicle

class Homework(models.Model):
    姓名 = models.ForeignKey(Student, on_delete=models.CASCADE)
    学号 = models.CharField(max_length=13, default = '填写学号')
    离校日期 = models.DateField()
    目的地 = models.CharField(max_length=200, default = '省份')
    交通工具 = models.ForeignKey(交通工具, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.学号

    