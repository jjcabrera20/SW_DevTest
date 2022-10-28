from django.db import models
from django_countries.fields import CountryField
import requests
# Create your models here.
SEX_CHOICES= (
('F','Female'),
('M','Male'),
('O','other'),
)

PARTNER_CHOICES = (
('Y','Yes'),
('N','No'),
)


class Beneficiaries(models.Model):
    surname = models.CharField(max_length=200)
    given_name = models.CharField(max_length=200)
    sex = models.TextField(null=True, choices=SEX_CHOICES)
    date_of_birth = models.DateField()
    place_of_birth = CountryField()
    height = models.PositiveIntegerField(null=True)
    partner = models.TextField(null=True, choices=PARTNER_CHOICES)
    children = models.BooleanField(null=True)
    number_children = models.PositiveIntegerField()
