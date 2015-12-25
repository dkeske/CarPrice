from django.db import models

# Create your models here.
# kw, km, year, ac, gears, body, userPrice

class carAd(models.Model):
    kw = models.CharField(max_length=20)
    km = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    ac = models.CharField(max_length=20)
    gears = models.CharField(max_length=20)
    body = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    idFromSite = models.CharField(max_length=20)