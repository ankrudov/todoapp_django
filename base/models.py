from django.db import models

#this is how you import the dhango user models
from django.contrib.auth.models import User

# Create your models here.

class task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False) #automatically set to false, once task has been completed it becomes true 
    created = models.DateTimeField(auto_now_add=True) #date and time auto added as soon as the task is completed

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete'] #ordering by the complete variable
    