from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path("", login_required(views.Home.as_view()), name="home"),
    path("profile/<int:pk>", login_required(views.Profile.as_view()), name="profile"),
    path("computers/", login_required(views.Computer.as_view()), name="computers"),
    path("computerform/", login_required(views.ComputerForm.as_view()), name="computers-form"),
    path("transactions/", login_required(views.Transactions.as_view()), name="transactions"),
    path("users/", login_required(views.Users.as_view()), name="users"),
    path("staff/", login_required(views.Staff.as_view()), name="staff"),
    path(
        "togglestatusstaff/",
        login_required(views.ToggleStatusStaff.as_view()),
        name="toggle staff status",
    ),
]
