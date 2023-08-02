from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/users/', null=True, blank=True)
    
    def full_name(self):
        return self.user.get_full_name()
    def __str__(self):
        return self.username

class DepartmentModel(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.title

class DesignationModel(models.Model):
    title = models.CharField(max_length=60)
    responsibility = models.TextField()
    
    def __str__(self):
        return self.title

class BankDetails(models.Model):
    bank_name = models.CharField(max_length=120)
    branch = models.CharField(max_length=120)
    account_number = models.CharField(max_length=120)
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user
class UserDetailsModel(models.Model):
    employee_id = models.IntegerField()
    joining_date = models.DateField(auto_now_add=True)
    birth_date = models.DateField(null=True)
    department = models.ForeignKey(DepartmentModel, on_delete=models.DO_NOTHING)
    designation = models.ForeignKey(DesignationModel, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, null=True)
    salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        self.employee_id