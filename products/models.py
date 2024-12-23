from django.db import models

# Create your models here.
class ProductModel(models.Model):
    pid = models.CharField(max_length=5,primary_key=True)
    img = models.TextField()
    prod_name = models.CharField(max_length=10)
    description = models.TextField()
    price = models.CharField(max_length=10)
