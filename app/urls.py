from django.urls import include, path

from app.views import UserRegisterView, UserLoginView


urlpatterns = [
    path("", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    
]
