from django.urls import path 
from .views import TaskList

#urls cant use classes so we must use the function as_view 
urlpatterns = [
    path('',TaskList.as_view(),name='tasks'),
]
