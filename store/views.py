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
    if Game.objects.all().exists():
        context['Games'] = Game.objects.all()
    if request.user.is_authenticated():
        context['OwnedGames'] = UserInventory.objects.get(user=request.user).games.all()
    return render(request, "store.html", context)

def addgame_view(request, game_id = None):
    if(game_id == None):
        addgame = addgame_form(request.POST or None)
        context = {'form': addgame}
    else:
        try:
            game = Game.objects.get(pk = game_id)
            if(request.user == game.developer):
                addgame = addgame_form(request.POST or None, instance = game)
                context = {'form': addgame}
            else:
                context = {'error': "You are not the owner of this game..."}
        except:
                context = {'error': "This game does not exist..."}

    if request.method == 'POST':
        if addgame.is_valid():
            new_addgame = addgame.save(commit=False)
            new_addgame.developer = request.user
            new_addgame.save()
            users_inventory = UserInventory.objects.get(user = request.user)
            users_inventory.games.add(new_addgame)
            users_inventory.save()
            data = addgame.cleaned_data
            context = {'added': data['title']}
            return redirect('/', context)

    return render(request, "addgame.html", context)

@require_http_methods(["GET"])
def playgame_view(request, game_id):
    try:
        game = UserInventory.objects.get(user=request.user).games.get(pk = game_id)
        context = { 'game': game}
    except Game.DoesNotExist:
        try:
            game = Game.objects.get(pk = game_id)
            context = {'error': "You do not own this game !", 'redirect': game_id}
        except Game.DoesNotExist:
            context = {'error': "This game does not exist !"}

    return render(request, "playgame.html", context)

@require_http_methods(["GET"])
def deletegame_view(request, game_id):
    if request.user.is_authenticated():
        context = dict()
        try:
            game = UserInventory.objects.get(user=request.user).games.get(pk = game_id)
            if(request.user == game.developer):
                game.delete()
                context['success'] = "Game deleted succesfully !"
            else:
                context['error'] = "Not your game buddy!!"
        except Game.DoesNotExist:
            context['error'] =  "This game does not exist !"

        context['inventoryGames'] = UserInventory.objects.get(user=request.user).games.all()
        return render(request, "inventory.html", context)
    else:
        return redirect('/login/?next=' + request.path)
