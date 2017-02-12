from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.exceptions import ValidationError

from hashlib import md5
from decimal import Decimal

from django.conf import settings
from store.models import Game
from payments.models import Payment

TWOPLACES = Decimal(10) ** -2

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
      
      sid = settings.SELLER_ID
      pment = create_payment(request.user, game.price, sid)
      context['pid'] = pment.id
      context['sid'] = sid
      context['amount'] = pment.transaction
      context['checksum'] = pment.checksum
      context['success_url'] = settings.SUCCESS_URL
      context['error_url'] = settings.ERROR_URL
      context['cancel_url'] = settings.CANCEL_URL
      context['pay_url'] = settings.PAYMENT_URL

      return render(request, 'buy.html', context)
    else:
      return redirect('/login/?next=' + request.path)

def create_payment(user, price, sid):
  pment = Payment()
  pment.user = user
  pment.transaction = price
  pment.save()
  pment.checksum = hash(pment.id, sid, price)
  pment.save()
  return pment

@require_http_methods(["GET"])
def success(request, *args, **kwargs):
  
  context = dict()
  context['status'] = 'YES'
  return render(request, 'test.html', context)

@require_http_methods(["GET"])
def cancel(request, *args, **kwargs):
  context = dict()
  context['status'] = 'CANCEL'
  return render(request, 'test.html', context)

@require_http_methods(["GET"])
def error(request, *args, **kwargs):
  context = dict()
  context['status'] = 'NO'
  return render(request, 'test.html', context)

def hash(pid, sid, amount):
  checksumstr = "pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, settings.PAYMENT_KEY)
  m = md5(checksumstr.encode("ascii"))
  return m.hexdigest()