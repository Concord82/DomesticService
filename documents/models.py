from django.db import models
from catalogs.models import Goods
from person.models import Storages
from person.models import User

# Create your models here.
from django.utils.translation import ugettext_lazy as _

class TransferString(models.Model):
    name = models.ManyToManyField(Goods)
    kolvo = models.IntegerField(_('kol-vo'))

class Transfer(models.Model):
    move_from = models.ForeignKey(Storages, on_delete=models.SET_NULL, blank=True, null=True,related_name='+',)
    move_to = models.ForeignKey(Storages, on_delete=models.SET_NULL, blank=True, null=True,related_name='+',)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,)
    body = models.ManyToManyField(TransferString, )
