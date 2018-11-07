# -*- coding: utf-8 -*-
from django.contrib import admin
from bot1.models import ToDoList, TodoItem


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['name', 'context', 'createdTime', 'expiredTime']


admin.site.register(ToDoList, ToDoListAdmin)


class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ['item', 'todoList', 'status', 'remind_time']


admin.site.register(TodoItem, ToDoItemAdmin)