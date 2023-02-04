from django.db import models

# Create your models here.

# class Registration(models.model):
    # first_name=models.Charfield(max_length=200,null=True)
class Contact(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)

    def __str__(self):
        return self.first_name
    

