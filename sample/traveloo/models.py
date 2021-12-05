from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length = 50)
    img = models.ImageField(upload_to = 'pictures')
    desc = models.TextField(max_length = 200)
    price = models.IntegerField()
    offer = models.BooleanField(default = False)
