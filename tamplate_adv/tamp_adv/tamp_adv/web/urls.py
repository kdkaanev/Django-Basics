from django.urls import path

from tamp_adv.web import views

urlpatterns =(
    path('', views.index, name='web-index'),
    path('about/', views.about, name='web-about'),
)