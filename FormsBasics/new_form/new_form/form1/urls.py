from django.urls import path

from new_form.form1 import views
from new_form.form1.views import index

urlpatterns = (
    path('', index, name='form1'),
)