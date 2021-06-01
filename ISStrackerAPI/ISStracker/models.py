from django.db import models
import requests


class Pos_data(models.Model):
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    time = models.DateField()