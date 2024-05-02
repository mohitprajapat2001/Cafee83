from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path("payments/<int:computer_id>", login_required(views.Payments.as_view()), name="payments"),
    path("ordercomplete/<int:computer_id>", login_required(views.OrderCompleteView.as_view()), name="ordercomplete"),
   
]
