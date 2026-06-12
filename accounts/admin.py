from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Role",  {"fields":("role","image", "phone", "address" )}),
    )
    list_display = ('username','role')
    list_filter = ("role", "is_staff")