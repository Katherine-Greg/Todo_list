from django.contrib import admin
from django.urls import path, include

from todo_list_service.views import TaskListView, TagListView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "todo_list"
