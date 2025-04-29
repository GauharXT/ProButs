from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Кошумча маалымат', {'fields': ('phone_number', 'age')}),
    )
    list_display = ('username', 'email', 'is_staff')