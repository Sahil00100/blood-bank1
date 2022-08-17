from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.


class Person(models.Model):
    GROUPS = (
            ('A+','A+'),
            ('O+','O+'),
            ('B+','B+'),
            ('AB+','AB+'),
            ('A-','A-'),
            ('O-','O-'),
            ('B-','B-'),
            ('AB-','AB-'),
    )
    name=models.CharField(max_length=101)
    age=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    city=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    bloodgroup=models.CharField(max_length=100,choices=GROUPS)
    type_of_donor=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class BloodBank(models.Model):
    GROUPS=(
    ('A+','A+'),
    ('O+','O+'),
    ('B+','B+'),
    ('AB+','AB+'),
    ('A-','A-'),
    ('O-','O-'),
    ('B-','B-'),
    ('AB-','AB-'),
    )
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    city=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    bloodgroup=MultiSelectField(choices=GROUPS)
    type_of_donor=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    