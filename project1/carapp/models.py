from django.db import models

# Create your models here.
class car(models.Model):
    id=models.IntegerField(primary_key=True)
    brand=models.CharField(max_length=15)
    model=models.CharField(max_length=30)
    year=models.DateField()
    price=models.IntegerField()
    type=models.CharField(max_length=10)