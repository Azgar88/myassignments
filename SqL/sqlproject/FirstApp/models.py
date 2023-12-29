from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    mailid=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    confirmpassword=models.CharField(max_length=100)

