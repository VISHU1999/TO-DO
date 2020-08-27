from django.shortcuts import render
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView
# from todoapp.form import Creattask
from .models import *

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)


# Create your views here.
class Homepageview(ListView):
    template_name = 'todoapp/home.html'
    model = Task
    context_object_name = 'tasklist'


class Createtask(CreateView):
    template_name = 'todoapp/createform.html'
    success_url = '/home/'
    model = Task
    fields = ['task_title', 'task_details', 'task_status', ]


class Updatetask(UpdateView):
    template_name = 'todoapp/updateform.html'
    success_url = '/home/'
    fields = ['task_title', 'task_details', 'task_status', ]
    model = Task


class Deletetask(DeleteView):
    template_name = 'todoapp/deleteform.html'
    success_url = '/home/'
    model = Task
