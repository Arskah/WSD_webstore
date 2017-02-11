from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from store.models import Game
from store.models import UserInventory

def inventory_view(request, *args, **kwargs):
  if request.user.is_authenticated():
    context = dict()
    context['inventoryGames'] = UserInventory.objects.get(user=request.user).games.all()
    return render(request, "inventory.html", context)
  else:
    return redirect("/login/")

def shop_view(request, *args, **kwargs):
    context = dict()
    context['Games'] = Game.objects.all()
    if request.user.is_authenticated():
      context['OwnedGames'] = UserInventory.objects.get(user=request.user).games.all()
    else:
      context['OwnedGames'] = []
    return render(request, "store.html", context)
