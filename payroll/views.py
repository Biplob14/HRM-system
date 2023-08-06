from django.shortcuts import render
from django.views.generic import DetailView
from .models import MonthlyPayment
# Create your views here.

class PayrollView(DetailView):
    model = MonthlyPayment
    template_name = 'payroll.html'
    context_object_name = 'payroll_data'
    slug_field = 'slug'