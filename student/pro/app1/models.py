from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class students(models.Model):
    Name=models.CharField(max_length=200)
    Class=models.CharField(max_length=200)
    Image=models.ImageField(upload_to='gallery')
    DOB=models.CharField(max_length=200)
    Guardian=models.CharField(max_length=200)  
    
    def __str__(self):
        return self.Name