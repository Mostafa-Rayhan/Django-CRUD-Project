from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    varsity_id = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=10)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=15)
 