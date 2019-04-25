from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from rest_api import views

_urlpatterns = [
    path("latest/", views.LatestFirmwareView.as_view()),
    path("latest-after/<str:version>/", views.LatestFirmwareView.as_view()),
]

urlpatterns = format_suffix_patterns(_urlpatterns)
