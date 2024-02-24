from django.urls import path

from exam_app.web import views

urlpatterns = (
    path('', views.index, name='index'),
)