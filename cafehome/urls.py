from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.Home.as_view()),
    path("computers/", views.Computer.as_view()),
]
