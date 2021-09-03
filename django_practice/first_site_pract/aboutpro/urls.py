from django.urls import path
from . import views 

urlpatterns = [
    path('aboutproject', views.about_pro)
]