from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from rest_api import views

_urlpatterns = [
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("latest/", views.LatestFirmwareView.as_view()),
    path("latest-after/<str:version>/", views.LatestFirmwareView.as_view()),
]

urlpatterns = format_suffix_patterns(_urlpatterns)
