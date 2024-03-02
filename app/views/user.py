import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from app.forms import UserForm, UserLoginForm
from app.models import MyUser

logger = logging.getLogger(__name__)

class UserRegisterView(CreateView):
    template_name = "users/register.html"
    success_url = "login"
    form_class = UserForm

    def form_valid(self, form):
        
        password = form.cleaned_data.get("password")
        password_confirm = form.cleaned_data.get("password_confirm")
        
        if password != password_confirm:
            messages.error(self.request, "passwords are not the same")
            
            return self.form_invalid(form)
        username = form.cleaned_data.get("username")
        if MyUser.objects.filter(username=username).exists():
            messages.error(self.request, "A user with that username already exists")
            
            return self.form_invalid(form)
        else:
            messages.success(self.request, "the user account created successfully")
        return super().form_valid(form)
    

def loginview(request):
    if request.method == "POST":
        form = UserForm(request.POST)  # noqa
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
    return render(request, "users/login.html")

class HomeView(View):
    template_name = "users/home.html"
    
    def get(self, request):
        
        return render(request, self.template_name)