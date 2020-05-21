from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Form(models.Model):
    istaiga = models.CharField(max_length=200)
    formos_data = models.DateTimeField(auto_now_add=True, blank=True)
    komisijos_nariai = models.ManyToManyField(User)
    vieta = models.CharField(max_length=200)
    atsakingas_darbuotojas = models.ForeignKey(User, on_delete=models.CASCADE, related_name='atsakingas_darbuotojas')
    #---
    pardavejas = models.CharField(max_length=200)
    serija = models.CharField(max_length=200)
    numeris = models.IntegerField()
    pardavimo_data = models.DateTimeField()



class PvmForm(models.Model):
    pavadinimas = models.CharField(max_length=200)
    vnt = models.CharField(max_length=200)
    kiekis = models.IntegerField()
    kaina = models.FloatField()
    suma = models.FloatField()
    vieta = models.CharField(max_length=500)
    forma = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='pvmforms')
