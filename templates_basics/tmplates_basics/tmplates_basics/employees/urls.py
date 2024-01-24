from django.urls import path

from tmplates_basics.employees.views import index, employees_details

urlpatterns = (
    path("", index, name="index"),
    path("emploees/<pk>", employees_details, name="employees_details")
)