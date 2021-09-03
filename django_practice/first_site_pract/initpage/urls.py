from django.urls import path
from . import views

urlpatterns = [
    path('pathforinitpage/',views.welcome)
]