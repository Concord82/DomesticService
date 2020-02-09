from django.contrib import admin
from .models import TransferString, Transfer
# Register your models here.

@admin.register(TransferString)
class TransferStringAdmin(admin.ModelAdmin):
    pass


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    pass