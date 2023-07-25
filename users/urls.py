from django.urls import path
from .views import UserRegistration, UserLogin, EmployeeList

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user_register'),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('employees/', EmployeeList.as_view(), name='employe_list'),
]
