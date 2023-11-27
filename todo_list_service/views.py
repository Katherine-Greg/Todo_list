from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from todo_list_service.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TagListView(generic.ListView):
    model = Tag
