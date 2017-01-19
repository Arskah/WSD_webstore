from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # https://docs.djangoproject.com/en/1.10/ref/contrib/auth/
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_delete
#from datetime import datetime
#from io import StringIO
#import csv

class StoreUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    publisher = models.BooleanField(default=False,)  # has own games for sale? -> if more info needed from devs we can create own model
    verified = models.BooleanField(default=False,) # check if the user has verified the account through email.

    def __str__ (self):
        return self.user.username

    def Meta():
        verbose_name = "Store user"
        verbose_name_plural = "Store users"

#When StoreUser is deleted, so is the User.
@receiver(post_delete, sender=StoreUser)
def post_delete_user(sender, instance, *args, **kwargs):
    if instance.user: # just in case user is not specified
        instance.user.delete()

class Game(models.Model):
    title = models.CharField(max_length=127,)
    url = models.URLField(blank=True,)
    image_url = models.URLField(blank=True,)
    developer = models.ForeignKey(StoreUser, related_name = "games", related_query_name = "game")    # creator of game, games can now be queried per storeuser. (https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.related_name)
    created = models.DateTimeField(default=timezone.now,)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0) #max price 999, cents possible
    description = models.CharField(max_length= 255,)
    raters = models.ManyToManyField(StoreUser,)
    ratingsum = models.IntegerField(default = 0)
    rating = models.IntegerField(default = 0)

    CATEGORY_CHOISES = [
    ('ACTION', "Action"),
    ('ADVENTURE', "Adventure"),
    ('ARCADE', "Arcade"),
    ('BOARD', "Board"),
    ]

    category = models.CharField(max_length = 12, choices = CATEGORY_CHOISES)

#Function to rate the game. Return True if rating succeeded, false if the user has already rated.
    def rate(self,rating,obj):
        if rating > 0 and rating <= 5:
            if self.raters.filter(pk = obj.pk).exists():
                return False
            else:
                self.raters.add(obj)
                self.ratingsum = self.ratingsum + rating
                self.rating = self.ratingsum/self.raters.count()
                self.save()
                return True

class UserInventory():
    user = models.OneToOneField(StoreUser, on_delete=models.CASCADE, related_name='inventory', primary_key=True,)
    games = models.ForeignKey(Game,)
