from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _
from django_summernote.admin import SummernoteModelAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm, OfficesForm
from .models import User, Clients, Offices


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('get_short_name', 'phone', 'email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
            'last_name',
            'first_name',
            'middle_name',

            'phone',
            'address',
            'birthDay',
            'avatar',
            'image_tag',
            'position'
        )}),
        ('Permissions', {'fields': ('is_admin', 'is_active', )}),
    )
    readonly_fields = ['image_tag']
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)


@admin.register(Clients)
class AdminClients(SummernoteModelAdmin):
    list_display = ('get_short_name','get_phone_number',)
    fieldsets = (
                    (_('Personal info'),{'fields': (
                        (
                            'last_name',
                            'first_name',
                            'middle_name'
                        ),
                        'phone',
                    )}),
                    (_('Other info'), {'fields': (
                        (
                            'email',
                            'address'),
                        'birthDay',
                        'comment',
                        'ranks',
                        (
                            'creationData',
                            'lastAction')
                    )})
    )
    readonly_fields = ['creationData','lastAction', ]
    search_fields = ('last_name', 'phone')
    list_filter = ('lastAction',)
    summernote_fields = ('comment',)


@admin.register(Offices)
class OfficesAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_code', 'address','phone','clock_work', 'enabled',)
    form = OfficesForm
