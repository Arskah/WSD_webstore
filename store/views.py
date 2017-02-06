from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Game
from .models import UserInventory

def inventory_view(request, *args, **kwargs):
  if request.user.is_authenticated():
    inventoryGames = UserInventory.objects.get(pk=request.user).games.objects.all()
    return render(request, "inventory.html")
  else:
    return redirect("registeration/login.html")

def shop_view(request, *args, **kwargs):
    allGames = Game.objects.all()
    return render(request, "store.html")
