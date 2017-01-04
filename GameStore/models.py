from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # https://docs.djangoproject.com/en/1.10/ref/contrib/auth/
#from datetime import datetime
#from io import StringIO
#import csv

class StoreUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now,)
    publisher = models.BooleanField(default=False,)  # has own games for sale? -> if more info needed from devs we can create own model

class Game(models.Model):
    title = models.CharField(max_length=127,)
    url = models.URLField(blank=True,)
    image_url = models.URLField(blank=True,)
    developer = models.ForeignKey(StoreUser,)    # creator of game
    created = models.DateTimeField(default=timezone.now,)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0) #max price 999, cents possible

class UserInventory():
    user = models.OneToOneField(StoreUser, on_delete=models.CASCADE, primary_key=True,)
    games = models.ForeignKey(Game,)