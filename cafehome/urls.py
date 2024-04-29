from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.Home.as_view(), name="home"),
    path("profile/", views.Profile.as_view(), name="profile"),
    path("computers/", views.Computer.as_view(), name="computers"),
    path("addcomputers/", views.AddComputer.as_view(), name="add-computers"),
    path("transactions/", views.Transactions.as_view(), name="transactions"),
    path("users/", views.Users.as_view(), name="users"),
    path("staff/", views.Staff.as_view(), name="staff"),
    path("togglestatusstaff/", views.ToggleStatusStaff.as_view(), name="toggle staff status"),
]
