from typing import Any
from django import forms

from app.models import MyUser


class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput())
    password_confirm = forms.CharField( max_length=30, required=True, widget=forms.PasswordInput())
    class Meta:
        model = MyUser
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "password_confirm",
        ]
   

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = [
            "username",
            "password",
        ]