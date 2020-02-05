from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SocialLink
# Register your models here.

@admin.register(SocialLink)
class SocialLinksAdmin(SortableAdminMixin, admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('my_order','socialtype', 'url', 'enabled',)
    list_editable =('url', 'enabled',)
    list_filter = ('socialtype',)
