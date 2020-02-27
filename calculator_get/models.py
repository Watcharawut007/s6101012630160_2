from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Calculate_get(models.Model):
    num1 = models.IntegerField(default=0)
    num2 = models.IntegerField(default=0)
    operate = models.TextField(blank=True)
    result = models.IntegerField(default=0)
    def calculate(self,int1,int2,operate2,result2):
        self.num1 = int1
        self.num2 = int2
        self.operate = operate2
        self.result =result2
        self.save()