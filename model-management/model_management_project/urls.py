from django.contrib import admin
from django.urls import path
from model_app.views import HealthView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/health/", HealthView.as_view(), name="health"),
]