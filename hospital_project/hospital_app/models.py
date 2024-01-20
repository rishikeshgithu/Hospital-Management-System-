# hospital_app/models.py
from django.db import models

class Patient(models.Model):
    # Your Patient model fields and definitions go here
    id = models.CharField(max_length=3, primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    contactNumber = models.CharField(max_length=11)
    emailAdress = models.EmailField()
    history = models.CharField(max_length=255)
    doctor = models.CharField(max_length=100)
