from unicodedata import category
from django.db import models

# Create your models here.

class Product(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=255)
    price=models.FloatField()
    quantity=models.FloatField(blank=True,null=True)
    category=models.CharField(max_length=255, blank=True,null=True)
    accessories=models.CharField(max_length=255, blank=True,null=True)
    games=models.CharField(max_length=255, blank=True,null=True)
    des=models.CharField(max_length=500)
    image=models.FileField(upload_to="static/images/home",default="default.jpg")


    class Meta:
        db_table="product"

