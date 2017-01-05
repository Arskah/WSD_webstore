from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # https://docs.djangoproject.com/en/1.10/ref/contrib/auth/
from django.db.models.signals import post_save
#from datetime import datetime
#from io import StringIO
#import csv

class StoreUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #created = models.DateTimeField(default=timezone.now,). user.date_joined can be used as created.
    publisher = models.BooleanField(default=False,)  # has own games for sale? -> if more info needed from devs we can create own model
    verified = models.BooleanField(default=False,) # check if the user has verified the account through email.

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        StoreUser.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

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
