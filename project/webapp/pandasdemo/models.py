from django.db import models

# Create your models here.

class Orders(models.Model):
    id_order=models.IntegerField()
    client_name=models.CharField(max_length=200)
    client_surname=models.CharField(max_length=200)
    order_date=models.CharField(max_length=200)
    price=models.IntegerField()