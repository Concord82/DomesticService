from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class gdsCategories(MPTTModel):
    name = models.CharField(_('Category Name'), max_length=32)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('gdsCategory')
        verbose_name_plural = _('gdsCategories')

class Goods(models.Model):
    UNIT_CHOISE = (
        (1, _('thing')),
        (2, _('meter')),
        (3, _('packaging')),
    )
    gdsCategories =TreeForeignKey(gdsCategories, on_delete=models.CASCADE)
    name = models.CharField(_('Goods'), max_length=100, unique=True)
    vendor_code = models.CharField(_('Vendor Code'), max_length=32, blank=True)
    unit = models.IntegerField(_('Unit'), choices=UNIT_CHOISE)
    price = models.DecimalField(_('Price'), max_digits=8, decimal_places=2, default=0)
    description = models.TextField(_('Deskription'), blank=True)
    photo = models.ImageField(_('Photo') ,upload_to='goods/', default='../static/images/nophoto.jpg')

    @property
    def price_display(self):
        return _('$ %s') % self.price

    @property
    def price_display_full(self):
        if self.price > 999:
            return _('$ %s %s.%s') % (str(self.price)[:-6] , str(self.price)[-6:-3], str(self.price)[-2:] )
        return _('$ %s') % self.price

    class Meta:
        verbose_name = _('Good')
        verbose_name_plural = _('Goods')


class Products(MPTTModel):
    name = models.CharField(_('Category Name'), max_length=32)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class Operations(MPTTModel):
    name = models.CharField(_('Category Name'), max_length=32)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('Operation')
        verbose_name_plural = _('Operations')


class PriceOperations(models.Model):
    product = TreeForeignKey(Products, on_delete=models.CASCADE)
    opearation = TreeForeignKey(Operations, on_delete=models.CASCADE)
    price = models.DecimalField(_('Price'), max_digits=8, decimal_places=2, default=0)

    @property
    def price_display(self):
        return _('$ %s') % self.price

    @property
    def price_display_full(self):
        if self.price > 999:
            return _('$ %s %s.%s') % (str(self.price)[:-6] , str(self.price)[-6:-3], str(self.price)[-2:] )
        return _('$ %s') % self.price

    def __str__(self):  # __unicode__ on Python 2
        return self.product.name + ' - ' + self.opearation.name

    class MPTTMeta:
        order_insertion_by = ['id']

    class Meta:
        verbose_name = _('Price Operation')
        verbose_name_plural = _('Price Operations')
