from django.urls import path
from .views import PayrollView


urlpatterns = [
    path('<slug:slug>/', PayrollView.as_view(), name='payroll'),
]
