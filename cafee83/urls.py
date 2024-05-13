# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from schema_graph.views import Schema
from django.conf.urls.static import static
from django.views.generic import RedirectView
from cafee83.settings import STATIC_ROOT, STATIC_URL, MEDIA_ROOT, MEDIA_URL

handler404 = "cafehome.views.error_404"
handler500 = "cafehome.views.error_500"

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", RedirectView.as_view(url="/home")),
    path("home/", include("cafehome.urls")),
    path("accounts/", include("users.urls")),
    path("paypal/", include("payments.urls")),
    path("schema", Schema.as_view()),
]

urlpatterns = urlpatterns + static(STATIC_URL, document_root=STATIC_ROOT)
urlpatterns = urlpatterns + static(MEDIA_URL, document_root=MEDIA_ROOT)
