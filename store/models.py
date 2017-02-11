from django.db import models
from django.utils import timezone
from users.models import StoreUser

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=127,)
    url = models.URLField(blank=True,)
    image_url = models.URLField(blank=True,)
    developer = models.ForeignKey(StoreUser, related_name = "games", related_query_name = "game")    # creator of game, games can now be queried per storeuser. (https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.related_name)
    created = models.DateTimeField(default=timezone.now,)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0) #max price 999, cents possible
    description = models.CharField(max_length= 255,)
    raters = models.ManyToManyField(StoreUser,blank = True)
    ratingsum = models.IntegerField(default = 0)
    rating = models.IntegerField(default = 0)

    CATEGORY_CHOISES = [
    ('ACTION', "Action"),
    ('ADVENTURE', "Adventure"),
    ('ARCADE', "Arcade"),
    ('BOARD', "Board"),
    ('DRIVING', "Driving"),
    ('STRATEGY',"Strategy"),
    ('HORROR',"Horror")
    ]

    category = models.CharField(max_length = 12, choices = CATEGORY_CHOISES)

    def __str__ (self):
        return self.title

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
