from django.urls import path
from .views import summary_api

urlpatterns = [
    path('summary/', summary_api),
]
