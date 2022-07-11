from django.db import models

# Create your models here.

class playstation(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=255)
    price=models.FloatField()
    quantity=models.FloatField(blank=True,null=True)
    des=models.CharField(max_length=255)
    image=models.FileField(upload_to="static/images/playstation",default="default.jpg")


    class Meta:
        db_table="playstation"

