from django.urls import path 
from .views import TaskList, TaskDetail

#urls cant use classes so we must use the function as_view 
urlpatterns = [
    path('',TaskList.as_view(),name ='tasks'),
    #view looks for the primary key in paths 'pk'
    path('task/<int:pk>/',TaskDetail.as_view(),name ='task'),
]
