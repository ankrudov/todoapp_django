from django.shortcuts import render
#importing list view to return query views
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView 
from django.urls import reverse_lazy #redirects user to another page after submitting 
from .models import task

#inheriting the listview functionality, by default it looks for a task_list.html file
class TaskList(ListView):
    model =  task
    context_object_name = 'tasks'

#by default detail view looks for task_detail.html file in the 'base' folder
class TaskDetail(DetailView):
    model = task
    context_object_name = 'task' #renaming object to more easily use django logic with html 


#by default this class looks for a file named task_form.html
class TaskCreate(CreateView):
    model = task
    fields = '__all__' #pulls all fields from the django model
    success_url = reverse_lazy('tasks') #if the submissions are successful, redirect user back to the tasks url

