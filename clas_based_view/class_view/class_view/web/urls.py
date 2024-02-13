from django.urls import path

from class_view.web import views
from class_view.web.views import index, CreateTodoView

urlpatterns = [
path('', index, name='index'),
    path('create/', CreateTodoView.as_view(), name='todos_create'),
]
