from django.db import models

# Create your models here.

class User_data_model(models.Model):
    username= models.CharField(max_length=255)
    age= models.IntegerField()
    # int-> more than digits -> out of range of int
    mobile_number= models.CharField(max_length=10)
    email= models.EmailField()
