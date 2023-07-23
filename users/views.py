from django.shortcuts import render
from django.views.generic import CreateView
from .models import UserModel
from .forms import UserRegistrationForm
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
class UserRegistration(CreateView):
    model = UserModel
    form_class = UserRegistrationForm
    success_url = reverse_lazy('user_register')
    template_name    = 'registration.html'
