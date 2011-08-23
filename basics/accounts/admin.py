from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from basics.accounts.models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    readonly_fields = ['creation_date', 'last_mod_date']


class NewUserAdmin(UserAdmin):
    inlines = UserAdmin.inlines + [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)

