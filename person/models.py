from __future__ import unicode_literals

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils.html import mark_safe
from django.core.exceptions import ValidationError
from django.db import models

from .managers import UserManager
# Create your models here.


def validate_phone(value):
    import re
    '''
    Номер телефона должен быть:
    ^\d{6}$ - только цифры 6 знаков для городских номеров
    ^[9]\d{9}$ - 10 цифр начинается на девятку
    ^[7-8][9]\d{9}$ - 11 цифр начинается на 7 или 8 потом 9 и еще 9 знаков
    ^\+[7][9]\d{9}$ - 12 знаков в федеральном формате на +7 
    '''
    reg = re.compile('^\d{6}$|^[9]\d{9}$|^[7-8][9]\d{9}$|^\+[7][9]\d{9}$')
    if not reg.match(value):
        raise ValidationError(_(u'%s hashtag doesnot comply' % value))


class User(AbstractBaseUser, PermissionsMixin):
    TITLE_CHOICE = (
        (1, _('administrator')),
        (2,_('master')),
        (3,_('manager'))
    )

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30)
    middle_name = models.CharField(_('Middle Name User'), max_length=64)
    last_name = models.CharField(_('last name'), max_length=30)
    phone = models.CharField(_('Phone Number'), max_length=12, unique=True, validators=[validate_phone])
    address = models.CharField(_('Address'), max_length=64, blank=True)
    position = models.IntegerField(_('Position in company'), choices=TITLE_CHOICE,default=2)
    birthDay = models.DateField(_('User BirthDay'), blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    avatar = models.ImageField(verbose_name=_('Photo'), upload_to='users/', default='../static/images/avatar/women.jpg')

    is_active = models.BooleanField(_('active'), default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        # The user is identified by their email address
        return self.last_name + ' ' + self.first_name + ' ' + self.middle_name

    def get_short_name(self):
        # The user is identified by their email address
        if self.first_name != '' and self.middle_name != '' and self.last_name != '':
            return self.last_name + ' ' + self.first_name[0] + '.' + self.middle_name[0] + '.'
        else:
            return self.email

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.avatar))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


    def __str__(self):  # __unicode__ on Python 2
        return self.get_short_name()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def save(self, *args, **kwargs):
        if len(self.phone) == 6:
            self.phone = '+73822' + self.phone
        elif len(self.phone) == 10:
            self.phone = '+7' + self.phone
        elif len(self.phone) == 11:
            if self.phone[0] == '7' or self.phone[0] == '8':
                self.phone = '+7' + self.phone[1:]
        super(User, self).save(*args, **kwargs)


class Clients(models.Model):
    first_name = models.CharField(_('first name'), max_length=30)
    middle_name = models.CharField(_('Middle Name User'), max_length=64)
    last_name = models.CharField(_('last name'), max_length=30)
    phone = models.CharField(_('Phone Number'), max_length=12, unique=True, validators=[validate_phone])
    email = models.EmailField(_('email address'), unique=True, blank=True)
    address = models.CharField(_('Address'), max_length=64, blank=True)
    birthDay = models.DateField(_('User BirthDay'), blank=True, null=True)
    creationData = models.DateTimeField(_('Registration Data'), auto_now_add=True)
    lastAction = models.DateTimeField(_('Last Action Data'), blank=True, null=True)
    comment = models.TextField(_('Comment'), blank=True)
    ranks = models.IntegerField(_('Clients ratio'), default=0)

    def get_full_name(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.middle_name

    get_full_name.short_description = _('Full Name User')

    def get_short_name(self):
        return self.last_name + ' ' + self.first_name[0] + '.' + self.middle_name[0] + '.'

    get_short_name.short_description = _('Short Name User')

    def get_phone_number(self):
        if self.phone[0:6] == '+73822':
            return '+7 (3822) ' + self.phone[6:9] + '-' + self.phone[9:]
        else:
            return self.phone[0:2] + '-' + self.phone[2:5] + '-' + self.phone[5:8] + '-' + self.phone[8:]

    get_phone_number.short_description = _('Phone Number')

    def comment_preview(self):
        coment_list = self.comment.split(' ')
        if len(coment_list) > 5:
            return ' '.join(coment_list[:5])
        else:
            return self.comment

    def clean(self):
        if len(self.phone) == 6:
            self.phone = '+73822' + self.phone
        elif len(self.phone) == 10:
            self.phone = '+7' + self.phone
        elif len(self.phone) == 11:
            if self.phone[0] == '7' or self.phone[0] == '8':
                self.phone = '+7' + self.phone[1:]

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        self.middle_name = self.middle_name.capitalize()
        super(Clients, self).save(*args, **kwargs)

    def __str__(self):
        return self.get_short_name()

    class Meta:
        verbose_name = _(u'Client')
        verbose_name_plural = _(u'Clients')
