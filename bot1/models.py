from django.db import models


class ToDoList(models.Model):
    name = models.CharField(max_length=150)  # todoList name
    context = models.TextField()  # todoList context
    createdTime = models.DateTimeField()   # createdTime
    expiredTime = models.DateTimeField()   # expiredTime
