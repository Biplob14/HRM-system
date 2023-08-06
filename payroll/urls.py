from django.urls import path
from .views import PayrollView


urlpatterns = [
    path('', PayrollView.as_view(), name='payroll'),
]
