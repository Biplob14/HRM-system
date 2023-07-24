from django.contrib import admin
from .models import UserModel
# Register your models here.

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'first_name',
        'last_name',
        'email',
    ]
    list_editable = [
        'first_name',
        'last_name',
    ]