from django.db import models
from users.models import UserModel, UserDetailsModel

# Create your models here.
class MonthlyPayment(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    allowance_reason = models.CharField(max_length=256, null=True, blank=True)
    allowance_amount = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, default=0)
    deduction_reason = models.CharField(max_length=256, null=True, blank=True )
    deduction_amount = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, default=0)
    month = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user

class TaxPercentage(models.Model):
    tax_percent = models.DecimalField(max_digits=4, decimal_places=2)
    minimum_amount = models.DecimalField(max_digits=8, decimal_places=2)

    def save(self):
        # count will have all of the objects from the Aboutus model
        count = TaxPercentage.objects.all().count()
        # this will check if the variable exist so we can update the existing ones
        save_permission = TaxPercentage.has_add_permission(self)

        # if there's more than two objects it will not save them in the database
        if count < 1:
            super(TaxPercentage, self).save()
        elif save_permission:
            super(TaxPercentage, self).save()

    def has_add_permission(self):
        return TaxPercentage.objects.filter(id=self.id).exists()
    
    def __str__(self):
        return "Tax Percentage"
