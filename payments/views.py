from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.exceptions import ValidationError

from hashlib import md5
from decimal import Decimal

from django.conf import settings
from store.models import Game, UserInventory
from payments.models import Payment

# Create your views here.
def buy_view(request, *args, **kwargs):
  if request.user.is_authenticated():
    if request.method == 'GET':
      # get object by id or give 404
      idx = kwargs.pop("idx", None)
      try:
        game = Game.objects.get(pk=idx)
        context = dict()
        context['game'] = game
      except Game.DoesNotExist:
        resp = HttpResponse('{"error":"Game not found!"}')
        resp.status_code = 404
        return resp

      # if user has the game, buy view of game not allowed
      try:
        UserInventory.objects.get(user = request.user).games.get(pk=idx)
        return redirect('/')
      except:
        pass

      sid = settings.SELLER_ID
      pment = create_payment(request.user, game, sid)
      context['pid'] = pment.id
      context['sid'] = sid
      context['amount'] = pment.transaction
      context['checksum'] = hash(pment.id, sid, pment.transaction)
      context['success_url'] = settings.SUCCESS_URL
      context['error_url'] = settings.ERROR_URL
      context['cancel_url'] = settings.CANCEL_URL
      context['pay_url'] = settings.PAYMENT_URL

      return render(request, 'buy.html', context)
    else:
      return redirect('/')
  else:
    return redirect('/login/?next=' + request.path)

def create_payment(user, game, sid):
  pment = Payment()
  pment.user = user
  pment.transaction = game.price
  pment.game = game
  pment.save()
  return pment

@require_http_methods(["GET"])
def success(request, *args, **kwargs):
  pid = request.GET["pid"]
  ref = request.GET["ref"]
  result = request.GET["result"]
  if request.GET["checksum"] == hash2(pid, ref, result):
    # Set status for payment
    pment = Payment.objects.get(pk = pid)
    pment.set_success(ref)

    # Add purchase for user
    inventory = UserInventory.objects.get(user = pment.user)
    inventory.games.add(pment.game)

    #redirect to game page
    return redirect('/')
  return HttpResponseBadRequest()

@require_http_methods(["GET"])
def cancel(request, *args, **kwargs):
  pid = request.GET["pid"]
  ref = request.GET["ref"]
  result = request.GET["result"]
  if request.GET["checksum"] == hash2(pid, ref, result):
    pment = Payment.objects.get(pk = pid)
    pment.set_cancel(ref)

    #give cancel notyfication
    #redirect to purchase screen
    return redirect('/')
  return HttpResponseBadRequest()

@require_http_methods(["GET"])
def error(request, *args, **kwargs):
  pid = request.GET["pid"]
  ref = request.GET["ref"]
  result = request.GET["result"]
  if request.GET["checksum"] == hash2(pid, ref, result):
    pment = Payment.objects.get(pk = pid)
    pment.set_error(ref)

    #todo: add error message
    #redirect to store
    return redirect('/')
  return HttpResponseBadRequest()

def hash(pid, sid, amount):
  return md5("pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, settings.PAYMENT_KEY).encode("ascii")).hexdigest()

def hash2(pid, ref, result):
  return md5("pid={}&ref={}&result={}&token={}".format(pid, ref, result, settings.PAYMENT_KEY).encode("ascii")).hexdigest()
