from django.contrib import admin
from .models import TaxPercentage, MonthlyPayment
from users.models import UserDetailsModel, UserModel
# Register your models here.

@admin.register(TaxPercentage)
class TaxPercentageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        base_add_permission = super(TaxPercentageAdmin, self).has_add_permission(request)
        if base_add_permission:
            # if there's already an entry, do not allow adding
            count = TaxPercentage.objects.all().count()
            if count == 0:
                return True
        return False

@admin.register(MonthlyPayment)
class MonthlyPaymentAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)