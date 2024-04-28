from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.Home.as_view(), name="home"),
    path("profile/", views.Profile.as_view(), name="profile"),
    path("computers/", views.Computer.as_view(), name="computers"),
]
