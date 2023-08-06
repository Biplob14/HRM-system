from django.shortcuts import render
from django.views.generic import CreateView
from .models import MonthlyPayment
# Create your views here.

class PayrollView(CreateView):
    model = MonthlyPayment
    template_name = 'payroll.html'
    context_object_name = 'payroll_data'

    def post(self, request, **args, **kwargs):
        pass
