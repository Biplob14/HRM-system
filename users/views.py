from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import UserModel
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
    template_name    = 'employee_list.html'