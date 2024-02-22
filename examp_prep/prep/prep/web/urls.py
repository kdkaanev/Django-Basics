from django import views
from django.urls import path

from prep.web.views import index,create_profile

urlpatterns = [
    path('', index, name='index'),
    path('create_profile/',create_profile, name='create_profile'),
]