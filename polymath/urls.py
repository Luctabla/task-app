from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todo_app.urls")),
    url(r"^auth/", include("rest_framework.urls", namespace="rest_framework")),
]
