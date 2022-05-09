from django.db import models

# Create your models here.
class Emplyoee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=100)
    eadd = models.CharField(max_length=100)
    esal = models.FloatField()
    image = models.ImageField()