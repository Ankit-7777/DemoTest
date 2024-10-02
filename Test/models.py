from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255) 
    email = models.EmailField(max_length=255, unique=True) 
    password = models.CharField(max_length=128) 

    def __str__(self):
        return self.name  
