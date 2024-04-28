from django.urls import path, include
from . import views

urlpatterns = [
    path("profile/", views.Profile.as_view(), name="home"),
    path("register/", views.Register.as_view(), name="register"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Login.as_view(), name="logout"),
    
]
