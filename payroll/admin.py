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
    readonly_fields=('gross_amount', 'tax_amount')
    exclude = [
        'slug',
    ]
    def save_model(self, request, obj, form, change):
        tax_amount = 0
        tax_data = TaxPercentage.objects.all()[0]
        selected_user = obj.user
        user_details_obj = UserDetailsModel.objects.get(user=selected_user)
        if user_details_obj.salary > tax_data.minimum_amount:
            tax_amount = (user_details_obj.salary * tax_data.tax_percent) / 100
        obj.gross_amount = user_details_obj.salary + obj.allowance_amount - obj.deduction_amount - tax_amount
        obj.tax_amount = tax_amount
        obj.slug = obj.user.username
        super().save_model(request, obj, form, change)