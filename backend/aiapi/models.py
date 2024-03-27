from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length =100)
    age = models.IntegerField(max_length =3)
    gender = models.CharField(max_length=10)
    height = models.IntegerField(max_length=3)
    weight = models.FloatField(max_length=3)
    ap_hi = models.IntegerField(max_length=3)
    ap_lo = models.IntegerField(max_length=3)
    cholesterol = models.IntegerField(max_length=1)
    gluc = models.IntegerField(max_length=1)
    smoke = models.IntegerField(max_length=1)
    alco = models.IntegerField(max_length=1)
    active = models.IntegerField(max_length=1)
    cardisrate= models.FloatField(max_length=1)
    
    def __str__(self) -> str:
        return self.name