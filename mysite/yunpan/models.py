from django.db import models

class Name(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Information(models.Model):
    离校日期 = models.DateField()
    目的地 = models.CharField(max_length=200)
    交通工具 = models.TextField()
    姓名 = models.ForeignKey(Name, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline