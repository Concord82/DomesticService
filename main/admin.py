from django.contrib import admin
from .models import SocialLink
# Register your models here.

@admin.register(SocialLink)
class SocialLinksAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('socialtype', 'url', 'enabled',)
    list_editable =('url', 'enabled',)