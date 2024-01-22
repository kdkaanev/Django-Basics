from django.urls import path

from URLs_and_views.department.views import department_details, department_by_name, redirect_to_softuni, \
    redirect_toindex_no_params, index, redirect_whit_params

urlpatterns = (
    path("redirekt_params/", redirect_whit_params, name='department_redirect'),
    path("index/", index),
    path('to-index/', redirect_toindex_no_params, name='department_index'),
    path("to-softuni/", redirect_to_softuni),
    path("<int:pk>/", department_details, name='department_details'),
    path("<str:name>/", department_by_name),



    )