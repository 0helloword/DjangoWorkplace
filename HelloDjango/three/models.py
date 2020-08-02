from django.db import models

class Grade(models.Model):
    g_name=models.CharField(max_length=20)

class Student(models.Model):
    s_name=models.CharField(max_length=20)
    s_grade=models.ForeignKey(Grade)