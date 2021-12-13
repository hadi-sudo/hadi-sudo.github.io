from django.db import models

# Create your models here.

class SmartPhone(models.Model):
    name= models.CharField(max_length=300)
    prix = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    image_url = models.TextField()
    def __str__(self):
        return self.firstname

