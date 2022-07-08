from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length= 200, null= True)
    email = models.CharField(max_length= 100, null= True)
    subject = models.CharField(max_length= 300, null = True)
    message = models.CharField(max_length= 500, null = True)