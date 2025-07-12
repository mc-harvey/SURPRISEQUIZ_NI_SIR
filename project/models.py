from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class project(models.Model):
    name=models.CharField()
    description=models.TextField()
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


