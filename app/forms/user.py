from django.forms import ModelForm

from app.models import MyUser


class UserForm(ModelForm):
    class Meta:
        model = MyUser
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]