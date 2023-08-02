from django.contrib import admin
from .models import UserModel, UserDetailsModel, DepartmentModel, DesignationModel, BankDetails
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

@admin.register(UserDetailsModel)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = [
        'employee_id',
        'joining_date',
        'birth_date',
        'department',
        'designation',
        'user',
        'salary',
    ]

@admin.register(DepartmentModel)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(DesignationModel)
class DesignationAdmin(admin.ModelAdmin):
    pass

@admin.register(BankDetails)
class BankDetailsAdmin(admin.ModelAdmin):
    pass