from django.urls import path

from forms.new import views

urlpatterns = (
    path('', views.index, name='index'),
    path('create-person/', views.create_person, name='create_person'),
    path('formset/', views.show_formset, name='formset'),
    )

