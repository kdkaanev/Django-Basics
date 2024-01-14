from django.http import HttpResponse
from django.shortcuts import render

from tasks.models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'task/index.html', context)