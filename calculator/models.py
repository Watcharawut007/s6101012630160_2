from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Subject(models.Model):
    num1 = models.IntegerField(default=0)
    num2 = models.IntegerField(default=0)
    operate = models.TextField(blank=True)
    result = models.IntegerField(default=0)