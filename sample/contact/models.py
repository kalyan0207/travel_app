from django.db import models
from django_countries.fields import CountryField

class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    country = CountryField(blank=True)
    subject = models.TextField(max_length=500)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.email_address