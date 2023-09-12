from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    provider = models.ForeignKey('Provider', null=True, on_delete=models.CASCADE)

class Provider(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
