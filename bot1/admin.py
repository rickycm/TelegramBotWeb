from django.contrib import admin
from bot1.models import ToDoList


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['name', 'context', 'createdTime', 'expiredTime']


admin.site.register(ToDoList, ToDoListAdmin)
