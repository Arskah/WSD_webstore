from django.db import models
from django.contrib.auth.models import AbstractUser # https://docs.djangoproject.com/en/1.10/ref/contrib/auth/
from django.db.models.signals import post_save
from django.db.models.signals import post_delete

class StoreUser(AbstractUser):
    publisher = models.BooleanField(default=False,)  # has own games for sale? -> if more info needed from devs we can create own model
    verified = models.BooleanField(default=False,) # check if the user has verified the account through email.

    def __str__ (self):
        return self.username

    def Meta():
        verbose_name = "Store user"
        verbose_name_plural = "Store users"

#When StoreUser is deleted, so is the User.
# @receiver(post_delete, sender=StoreUser)
# def post_delete_user(sender, instance, *args, **kwargs):
#     if instance.user: # just in case user is not specified
#         instance.user.delete()

# @receiver(post_save, sender=StoreUser, dispatch_uid="createUserInventory")
# def createUserInventory(sender, instance, created, **kwargs):
#   if (created):
#     inventory = UserInventory(instance)
#     inventory.save()
