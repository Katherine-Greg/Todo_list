from django.contrib import admin

from todo_list_service.models import Tag, Task

admin.site.register(Task)
admin.site.register(Tag)
