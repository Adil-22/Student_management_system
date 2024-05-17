from django.db import models

# Create your models here.

class Students(models.Model):
    
    name = models.CharField(max_length=70)
    father_name = models.CharField(max_length=70)
    phone = models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    address =models.CharField(max_length=500)

    
