from django import forms
from .models import UserModel


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "image"
        ]