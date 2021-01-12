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

class 学生信息(models.Model):
    full_name = models.CharField(max_length=70,default='', verbose_name='姓名')
    IP = models.CharField(max_length=13,default='', verbose_name='学号')
    #age = models.IntegerField()
    class Sex(models.IntegerChoices):
        MALE = 1, '男'
        FEMALE = 2, '女'
        OTHER = 3, '其他'

    sex = models.IntegerField(choices=Sex.choices)

    class Condition(models.IntegerChoices):
        healthy = 1, '健康'
        mess = 2, '有症状'
        OTHER = 3, '其他'

    condition = models.IntegerField(choices=Condition.choices)

    def __str__(self):
        return self.full_name

class 交通工具(models.Model):
    vehicle = models.CharField(max_length=70,default='', verbose_name='姓名')
    #age = models.IntegerField()
   
    def __str__(self):
        return self.vehicle

class homework(models.Model):
    姓名 = models.ForeignKey(学生信息, on_delete=models.CASCADE)
    学号 = models.CharField(max_length=13, default = '填写学号')
    班级 = models.CharField(max_length=20, default = '填写班级')
    离校日期 = models.DateField()
    目的地 = models.CharField(max_length=200, default = '省份')
    交通工具 = models.ForeignKey(交通工具, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.学号
        

    