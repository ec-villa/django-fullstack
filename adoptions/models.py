from djmoney.models.fields import MoneyField
from django.db import models
# Controls the data layer to construct our db schema and queries
# Create your models here.

class Pet(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ExampleData(models.Model):
    CURRENCY_CHOICES = [('USD', 'USD $'), ('EUR', 'EUR €')]
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    office = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    start_date = models.DateField()
    salary = MoneyField(max_digits=14, decimal_places=2, null=True, default_currency='EUR')
