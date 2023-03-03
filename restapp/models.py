from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    schedule = models.CharField(max_length=50)
    

class Patient(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.CharField(max_length=50)
    bgroup = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    

class Staff(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.CharField(max_length=50)