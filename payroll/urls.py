from django.urls import path
from .views import PayrollView

app_name = 'payroll'

urlpatterns = [
    path('<slug:slug>/', PayrollView.as_view(), name='payroll'),
]
