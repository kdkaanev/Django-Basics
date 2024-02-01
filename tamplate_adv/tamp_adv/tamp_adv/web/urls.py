from django.urls import path

from tamp_adv.web import views

urlpatterns =(
    path('', views.index, name='web-index'),
)