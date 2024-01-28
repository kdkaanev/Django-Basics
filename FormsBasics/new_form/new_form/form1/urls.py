from django.urls import path

from new_form.form1 import views
from new_form.form1.views import index

urlpatterns = (
    path('', index, name='index'),
    path('modelform/', views.index_models, name='index_models'),
    path('modelform/<int:pk>/', views.update_employee, name='update_employee'),
)