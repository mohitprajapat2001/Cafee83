# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path("payments/<int:computer_id>", views.Payments.as_view(), name="payments"),
    path(
        "ordercomplete/<int:computer_id>",
        views.OrderCompleteView.as_view(),
        name="ordercomplete",
    ),
]
