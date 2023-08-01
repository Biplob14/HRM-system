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

    def save_model(self, request, obj, form, change):
        password = form.cleaned_data.get('password')
        obj.set_password(password)
        super().save_model(request, obj, form, change)