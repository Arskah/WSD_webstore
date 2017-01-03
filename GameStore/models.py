from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from datetime import datetime
#from io import StringIO
#import csv

# class User(models.Model):
#     nick = models.CharField(max_length=127,)
#     email = models.EmailField()
#     created = models.DateTimeField(default=timezone.now,)
# #    inventory = models.ManyToManyField(Game)        #User.inventory.add(new_game)
#     publisher = models.BooleanField(default=False,)  # has own games for sale? -> if more info needed from devs then we can inherit the class

# class Game(models.Model):
#     title = models.CharField(max_length=127,)
#     url = models.URLField(blank=True,)
#     image_url = models.URLField(blank=True,)
#     developer = models.ForeignKey(User,)    # creator of game
#     created = models.DateTimeField(default=timezone.now,)
#     price = models.DecimalField(max_digits=5, decimal_places=2, default=0) #max price 999, cents possible

# class UserInventory():
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
#     games = models.ForeignKey(Game,)