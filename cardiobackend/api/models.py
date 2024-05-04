from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length =100)
    age = models.IntegerField(max_length =3)
    gender = models.IntegerField(max_length=10)
    height = models.IntegerField(max_length=3)
    weight = models.FloatField(max_length=30)      
    ap_hi = models.IntegerField(max_length=30)
    ap_lo = models.IntegerField(max_length=30)
    cholesterol = models.IntegerField(max_length=10)
    gluc = models.IntegerField(max_length=10)
    smoke = models.IntegerField(max_length=10)
    alco = models.IntegerField(max_length=10)
    active = models.IntegerField(max_length=10)
    cardisrate= models.FloatField(max_length=10)
    
    def __str__(self) -> str:
        return self.name
    
