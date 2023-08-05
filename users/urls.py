from django.urls import path
from .views import UserRegistration, UserLogin, EmployeeList, EmployeeDetaisl

app_name = 'users'

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user_register'),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('employees/', EmployeeList.as_view(), name='employe_list'),
    path('employees/<slug:slug>/', EmployeeDetaisl.as_view(), name='employe_details'),
]
