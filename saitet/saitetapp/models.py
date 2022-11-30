from django.db import models

class marks(models.Model):
    roll_num = models.CharField(max_length=13)
    name = models.CharField(max_length=50)
    marks = models.IntegerField(max_length=3)

