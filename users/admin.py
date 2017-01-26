from django.contrib import admin
from .models import StoreUser

#Register your admins here!

class StoreUserAdmin(admin.ModelAdmin):
    list_display = ('get_username','get_email','publisher','get_date')

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

    def get_date(self, obj):
        return obj.user.date_joined
    get_date.short_description = 'Created'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

admin.site.register(StoreUser, StoreUserAdmin)
