from django.db import models

class Student(models.Model):
    s_name=models.CharField(max_length=20)
    s_age=models.IntegerField(default=1)
