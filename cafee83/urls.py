# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from schema_graph.views import Schema
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", include("cafehome.urls")),
    path("accounts/", include("users.urls")),
    path("paypal/", include("payments.urls")),
    path("schema", Schema.as_view()),
]

urlpatterns = urlpatterns + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
