from django.urls import include, path

from app.views import UserRegisterView,  HomeView, loginview


urlpatterns = [
    path("", UserRegisterView.as_view(), name="register"),
    path("login/", loginview, name="login"),
    path('home/', HomeView.as_view(), name="home"),
    
]
