from django.urls import path
from . import views

urlpatterns = [
    path('firstpage/',views.firstpage)
]