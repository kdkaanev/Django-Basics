import json

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from class_view.web.models import Todo


# Create your views here.

def index(request):
    context = {
        'todo_list': [x.title for x in Todo.objects.all()],
    }
    return HttpResponse(json.dumps(context))


class CreateTodoView(views.CreateView):

    model = Todo
    fields = ['title', 'description', 'is_done']

    template_name = 'web/create_todo.html'

    success_url = reverse_lazy('index')