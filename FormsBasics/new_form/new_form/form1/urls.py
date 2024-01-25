from django.urls import path

from new_form.form1 import views

urlpatterns = (
    path('', views.index, name='form1'),
)