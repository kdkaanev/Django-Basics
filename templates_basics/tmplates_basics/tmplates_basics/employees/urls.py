from django.urls import path

from tmplates_basics.employees.views import index

urlpatterns = (
    path("", index, name="index"),
)