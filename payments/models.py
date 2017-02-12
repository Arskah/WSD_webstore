from django.db import models
from django.utils import timezone
from store.models import StoreUser

class Payment(models.Model):
  user = models.ForeignKey(StoreUser, related_name='buyer', blank=False, null=False,)
  created = models.DateTimeField(default=timezone.now,)
  transaction = models.DecimalField(max_digits=5, decimal_places=2,) #max price 999, cents possible
  status = models.CharField(max_length=7, default='ONGOING')
  checksum = models.CharField(max_length=32, default='')
  ref = models.IntegerField(default = -1)

  def set_success(self, ref):
    self.status = 'SUCCESS'
    self.ref = ref

  def set_error(self, ref):
    self.status = 'ERROR'
    self.ref = ref

  def set_cancel(self, ref):
    self.status = 'CANCEL'
    self.ref = ref