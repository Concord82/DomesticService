from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class SocialLink(models.Model):
    ''' ссылки на социальные сети выводимые на главной странице'''
    TYPE_SOCIAL = (
        (0, '---'),
        (1, 'twitter'),
        (2, 'facebook'),
        (3, 'instagram'),
        (4, 'google-plus'),
        (5, 'linkedin'),
        (6, 'whatsapp'),
        (7, 'vk'),
    )
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    socialtype = models.IntegerField(_('Social media'), choices=TYPE_SOCIAL, default=0)
    url = models.URLField(_('URL Adress Social media'))
    enabled = models.BooleanField(_('Enabled state'), default=False)

    def __str__(self):  # __unicode__ on Python 2
        return self.get_socialtype_display()

    class Meta:
        ordering = ['my_order']
        verbose_name = _('Social Net link')
        verbose_name_plural = _('Social Nets Links')


class TypeService(models.Model):
    title = models.CharField(_('title work'), max_length=32)
    slug = models.SlugField(_('Slug Link'), unique=True)
