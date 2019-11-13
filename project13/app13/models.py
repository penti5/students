from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=16)
    email = models.EmailField()

class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=16)
