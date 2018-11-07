# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser, Group


TODOITEMCHOICE = ((0,u'未完成'),(1,u'完成'),(2, u'正常'),(3, u'删除'),)

class ToDoList(models.Model):
    name = models.CharField(max_length=150)  # todoList name
    context = models.TextField()  # todoList context
    createdTime = models.DateTimeField(u'添加时间', auto_now_add=True)   # createdTime
    expiredTime = models.DateTimeField()   # expiredTime

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'待办列表'
        verbose_name_plural = u"待办列表"


class TodoItem(models.Model):
    item = models.CharField(u'事项', max_length=200, blank=False, null=False)
    #user = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    todoList = models.ForeignKey(ToDoList, null=False, default=0, on_delete=models.CASCADE)
    crt_time = models.DateTimeField(u'添加时间', auto_now_add=True)
    upd_time = models.DateTimeField(u'修改时间', null=True, auto_now_add=True)
    status = models.IntegerField(u'事项状态', choices=TODOITEMCHOICE, default=0)
    remind_time = models.DateTimeField(u'提醒时间', blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.item

    class Meta:
        verbose_name = u'事项'
        verbose_name_plural = u"事项"
