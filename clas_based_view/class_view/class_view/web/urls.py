from django.urls import path

from class_view.web import views
from class_view.web.views import CreateTodoView, ListTodoView

urlpatterns = [
    path('', ListTodoView.as_view(), name='todos-list'),
    path('create/', CreateTodoView.as_view(), name='todos-create'),
    path('<int:pk>/', views.DetailTodoView.as_view(), name='todos-details'),
    path('<slug:slug>/', views.DetailTodoView.as_view(), name='todos-details'),
    path('<int:pk>/<slug:slug>/', views.DetailTodoView.as_view(), name='todos-details'),

]
