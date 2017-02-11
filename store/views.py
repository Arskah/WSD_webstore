from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from store.models import Game,UserInventory
from .forms import addgame_form

def inventory_view(request, *args, **kwargs):
  if request.user.is_authenticated():
    context = dict()
    context['inventoryGames'] = UserInventory.objects.get(user=request.user).games.all()
    return render(request, "inventory.html", context)
  else:
    return redirect('/login/?next=' + request.path)

def shop_view(request, *args, **kwargs):
    context = dict()
    context['Games'] = Game.objects.all()
    if request.user.is_authenticated():
      context['OwnedGames'] = UserInventory.objects.get(user=request.user).games.all()
    else:
      context['OwnedGames'] = []
    return render(request, "store.html", context)

def addgame_view(request, *args, **kwargs):
    addgame = addgame_form(request.POST or None)

    if request.method == 'POST':
        if addgame.is_valid():
            new_addgame = addgame.save(commit=False)
            new_addgame.developer = request.user
            new_addgame.save()

            addgame.save()

            data = addgame.cleaned_data
            context = {'added': data['title']}
            return redirect('/', context)

    context = {'form': addgame}
    return render(request, "addgame.html", context)

@require_http_methods(["GET"])
def playgame_view(request, *args, **kwargs):
    return render(request, "main.html")
