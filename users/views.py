from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import UserModel, UserDetailsModel, BankDetails
from payroll.models import MonthlyPayment
from .forms import UserRegistrationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

# Create your views here.
class UserRegistration(CreateView):
    model = UserModel
    form_class = UserRegistrationForm
    success_url = reverse_lazy('user_register')
    template_name    = 'registration.html'

class UserLogin(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

class EmployeeList(ListView):
    model = UserModel
    template_name = 'employee_list.html'
    context_object_name = 'employee_list'

    def get_queryset(self):
        return UserDetailsModel.objects.select_related('user').all()

class EmployeeDetaisl(DetailView):
    model = UserDetailsModel
    context_object_name = 'employee_details'
    template_name = 'employee_details.html'
    slug_field = 'slug'

    def get_queryset(self):
        print("on user details query................")
        return UserDetailsModel.objects.select_related('user')
    
    def get_context_data(self, **kwargs):
        context = super(EmployeeDetaisl, self).get_context_data(**kwargs)
        user_data = list(self.get_queryset())[0].user
        context['bank_details'] = BankDetails.objects.filter(user=user_data).first()
        context['payroll'] = MonthlyPayment.objects.filter(user=user_data).last()
        # print("queryset: ", list(self.get_queryset())[0].user.username)
        return context