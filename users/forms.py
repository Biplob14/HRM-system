from django import forms
from .models import UserModel


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'