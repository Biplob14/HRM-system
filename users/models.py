from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
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
        return self.user.username
class UserDetailsModel(models.Model):
    employee_id = models.IntegerField(null=True)
    joining_date = models.DateField(auto_now_add=True)
    birth_date = models.DateField(null=True)
    department = models.ForeignKey(DepartmentModel, on_delete=models.DO_NOTHING, null=True)
    designation = models.ForeignKey(DesignationModel, on_delete=models.DO_NOTHING, null=True)
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, null=True)
    salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    slug = models.SlugField(max_length=256, blank=True, null=True)
    user_comment = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("users:employe_details", args=[self.slug])

    def __str__(self):
        return f"{self.employee_id}"