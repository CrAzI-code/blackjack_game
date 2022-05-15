from django.db import models

# Create your models here.

class PersonalData(models.Model):
    fullname = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    mothername = models.CharField(max_length=100)
    place_of_birth = models.CharField(max_length=300)
    state = models.CharField(max_length=100)
    time = models.TimeField(auto_now=False, auto_now_add=False,  blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True)