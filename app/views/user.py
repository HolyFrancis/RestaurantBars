from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from django.views import View
from django.shortcuts import render, redirect

from app.forms import UserForm, UserLoginForm
from app.models import MyUser


class UserRegisterView(CreateView):
    template_name = "users/register.html"
    success_url = "login"
    form_class = UserForm
    

class UserLoginView(View):
    template_name = "users/login.html"
    form_class = UserLoginForm
    
    def get(self, request):
        form = self.form_class
        
        return render(request, self.template_name, {"form": form})
    
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"],
                                password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect("home")
        message = "login failed"
        return render(request, self.template_name, {"form": form, "message": message})