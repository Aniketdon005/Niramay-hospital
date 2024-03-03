from django.db import models

# Create your models here.

class contact1(models.Model):
    
  cname = models.CharField(max_length = 50)
  cemail = models.EmailField()
  cmobile = models.BigIntegerField(max_length = 50)
  cage = models.IntegerField(max_length = 50)  
  cgender = models.CharField(max_length = 50)
  caddress = models.CharField(max_length = 50)
  
