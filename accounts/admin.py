from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email_confirmed']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('email_confirmed',)}),
    )
