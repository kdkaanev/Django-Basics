from django.urls import path

from URLs_and_views.department.views import department_details, department_by_name

urlpatterns = (
    path("<int:pk>/", department_details),
    path("<str:name>/", department_by_name)
)