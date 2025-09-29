# models.py
from django.db import models

class MyInfo(models.Model):
    phone=models.CharField(max_length=20)
    email=models.EmailField()
    def __str__(self):
        return f"{self.phone} and my email is {self.email} "
class Data(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return f"{self.name}"
class Mark(models.Model):
    mark=models.CharField(max_length=30)
    obj=models.CharField(max_length=30)
    def __str__(self):
        return f"{self.mark} {self.obj}"
