from django.db import models

# Create your models here.

class Details(models.Model):
    names = models.CharField(max_length=100)
    contact = models.IntegerField(primary_key=True)
    interests = models.CharField(max_length=300)
