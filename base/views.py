from django.shortcuts import render
#importing list view to return query views
from django.views.generic.list import ListView
from .models import task


#inheriting the listview functionality
class TaskList(ListView):
    model =  task