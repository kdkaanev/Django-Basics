import json
import random

from django import forms
from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic as views

from class_view.web.models import Todo


# Create your views here.


class FilterTodoForm(forms.Form):
    title_pattern = forms.CharField(
        max_length=Todo.MAX_TITLE_LENGTH,
        required=False,
    )
    is_done = forms.BooleanField(required=False)

class DetailTodoView(views.DetailView):
    model = Todo
    template_name = 'web/details_todo.html'


class ListTodoView(views.ListView):
    model = Todo
    queryset = Todo.objects.all()
    template_name = 'web/list_todo.html'
    paginate_by = 5



    def get_paginate_by(self, queryset):
        return super().get_paginate_by(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List Todo'
        context['filter_form'] = FilterTodoForm(
            initial={'title_pattern': self.get_title_pattern()}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.apply_filters(queryset)
        return queryset

    def get_title_pattern(self):
        return self.request.GET.get('title_pattern', None)

    def apply_filters(self, queryset):
        tittle_pattern = self.get_title_pattern()
        if tittle_pattern:
            queryset = queryset.filter(title__icontains=tittle_pattern)
        is_done = self.get_is_done()
        if is_done is not None:
            queryset = queryset.filter(is_done=is_done)
        return queryset

    def get_is_done(self):
        return self.request.GET.get('is_done', None) == 'on'


class CreateTodoView(views.CreateView):
    model = Todo
    fields = ['title', 'description', 'is_done']

    template_name = 'web/create_todo.html'

    success_url = reverse_lazy('todos-list')
