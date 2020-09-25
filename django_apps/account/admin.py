from django.contrib import admin
from django.contrib.auth.models import Group

from django.contrib.auth.admin import UserAdmin


from account.models import Account

admin.site.unregister(Group)

admin.site.site_header = "Billing Portal"
admin.site.site_title = "Billing AdminPortal"
admin.site.index_title = "Welcome to the admin panel of Billing"


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username',
                    'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {
            'fields': (('email', 'username'), 'date_joined', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'last_login')
        }),
        ('Permissions', {
            'classes': ('collapse', 'close'),
            'fields': (('is_active', 'is_staff'), ('is_admin', 'is_superuser'))
        }),

    )


admin.site.register(Account, AccountAdmin)
