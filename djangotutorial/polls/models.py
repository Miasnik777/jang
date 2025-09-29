# models.py
from django.db import models

class MyInfo(models.Model):
    phone=models.CharField(max_length=20)
    email=models.EmailField()
def __str__(self):
    return f"{self.phone} and my email is {self.email}"

