from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter, MPTTModelAdmin, TreeNodeChoiceField, MPTTAdminForm
from django_summernote.admin import SummernoteModelAdmin
import admin_thumbnails
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from .models import gdsCategories, Goods, Products, Operations, PriceOperations
# Register your models here.


@admin.register(gdsCategories)
class gdsCategoriesAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'something')
    list_display_links = ('something',)

    def something(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.name,  # Or whatever you want to put here
        )
    something.short_description = _('gdsCategories Description')


@admin.register(Goods)
@admin_thumbnails.thumbnail('photo')
class GoodsAdmin(SummernoteModelAdmin):
    list_display =('name', 'vendor_code', 'unit', 'price_display_full')
    search_fields = ('name','vendor_code',)
    list_filter =(
        ('gdsCategories', TreeRelatedFieldListFilter),
    )
    summer_note_fields = 'description'
    fieldsets = (
        (None, {
            'fields': ('gdsCategories', 'name', 'vendor_code', 'unit', 'price')
        }),
        ('Availability', {
            'fields': ('photo_thumbnail', 'photo', 'description')
        }),
    )


@admin.register(Products)
class ProductsAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'something')
    list_display_links = ('something',)
    def something(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.name,  # Or whatever you want to put here
        )

    something.short_description = _('Products Description')


@admin.register(Operations)
class OperationsAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'something')
    list_display_links = ('something',)
    def something(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.name,  # Or whatever you want to put here
        )
    something.short_description = _('Operations Description')


@admin.register(PriceOperations)
class PriceOperationsAdmin(admin.ModelAdmin):
    list_display =('product', 'opearation', 'price_display_full')
    list_filter =(
        ('product', TreeRelatedFieldListFilter),
        ('opearation', TreeRelatedFieldListFilter),
    )